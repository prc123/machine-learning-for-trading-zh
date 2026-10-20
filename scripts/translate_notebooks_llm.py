"""Translate notebook Markdown cells with an OpenAI-compatible chat API.

Code cells, outputs, metadata, and code comments are intentionally left
unchanged. Targets are written beside their sources as ``*.zh-CN.ipynb``.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import sys
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import requests


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ROOTS = [
    "02_financial_data_universe",
    "03_market_microstructure",
    "04_fundamental_alternative_data",
    "05_synthetic_data",
    "06_strategy_definition",
]

PROVIDERS = {
    "glm": ("https://open.bigmodel.cn/api/paas/v4", "glm-5.3-flash", "GLM_API_KEY"),
    "openai": ("https://api.openai.com/v1", "gpt-4o-mini", "OPENAI_API_KEY"),
    "deepseek": ("https://api.deepseek.com/v1", "deepseek-chat", "DEEPSEEK_API_KEY"),
    "moonshot": ("https://api.moonshot.cn/v1", "moonshot-v1-32k", "MOONSHOT_API_KEY"),
    "dashscope": (
        "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "qwen-plus",
        "DASHSCOPE_API_KEY",
    ),
    "openrouter": ("https://openrouter.ai/api/v1", "", "OPENROUTER_API_KEY"),
}

SYSTEM_PROMPT = """You are a professional translator for financial machine-learning notebooks.
Translate English Markdown into natural Simplified Chinese for an experienced quant reader.

Rules:
- Preserve Markdown structure, list nesting, tables, links, LaTeX, punctuation in formulas, and blank lines.
- Never translate inline code, code fences, identifiers, file paths, URLs, package names, column names, shell commands, or API names.
- Translate prose completely; do not summarize, add commentary, or omit sections.
- Use concise financial terminology. Keep an English term in parentheses when it is a domain term likely used by the code or book.
- Return only a valid JSON object mapping each input key to its translated Markdown string.
"""


class FatalAPIError(RuntimeError):
    """An API error that retrying cannot fix, such as an exhausted account."""

GLOSSARY = """
Preferred terms: feature=特征, label=标签, target=目标, universe=投资范围,
backtest=回测, transaction cost=交易成本, market microstructure=市场微观结构,
point-in-time=Point-in-Time (PIT), survivorship bias=幸存者偏差,
continuous contract=连续合约, roll=换月, synthetic data=合成数据,
strategy definition=策略定义. Keep "regime" in English unless the sentence is clearer as "市场状态".
"""


@dataclass(frozen=True)
class Segment:
    key: str
    text: str
    cache_key: str


@dataclass
class Stats:
    notebooks: int = 0
    translated: int = 0
    planned: int = 0
    skipped: int = 0
    failed: int = 0
    source_chars: int = 0
    cached_segments: int = 0
    api_segments: int = 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--provider",
        choices=sorted(PROVIDERS),
        default=os.getenv("TRANSLATION_PROVIDER", "glm"),
        help="Provider used only to choose default base URL and model.",
    )
    parser.add_argument("--base-url", default=os.getenv("TRANSLATION_API_BASE"))
    parser.add_argument("--api-key", default=os.getenv("TRANSLATION_API_KEY"))
    parser.add_argument("--model", default=os.getenv("TRANSLATION_MODEL"))
    parser.add_argument("--workers", type=int, default=4, help="Notebooks translated concurrently.")
    parser.add_argument("--max-chars", type=int, default=5000, help="Maximum source characters per API batch.")
    parser.add_argument("--max-segments", type=int, default=16, help="Maximum Markdown segments per API batch.")
    parser.add_argument("--temperature", type=float, default=0.15)
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--retries", type=int, default=5)
    parser.add_argument("--cache-dir", type=Path, default=REPO_ROOT / ".translation_cache")
    parser.add_argument(
        "--root",
        action="append",
        dest="roots",
        default=None,
        help="Chapter directory to translate. May be repeated. Defaults to chapters 02-06.",
    )
    parser.add_argument("--limit", type=int, default=0, help="Translate only the first N pending notebooks.")
    parser.add_argument("--overwrite", action="store_true", help="Regenerate existing zh-CN notebooks.")
    parser.add_argument("--dry-run", action="store_true", help="Show pending work without calling the API.")
    args = parser.parse_args()

    default_base, default_model, key_variable = PROVIDERS[args.provider]
    args.base_url = args.base_url or default_base
    args.model = args.model or default_model
    args.api_key = args.api_key or os.getenv(key_variable)
    if not args.model:
        parser.error("--model or TRANSLATION_MODEL is required for this provider")
    if not args.api_key and not args.dry_run:
        parser.error(
            "No API key found. Put TRANSLATION_API_KEY=... in .env.local, "
            f"or set {key_variable}."
        )
    if args.workers < 1 or args.max_chars < 500 or args.max_segments < 1:
        parser.error("--workers, --max-chars, and --max-segments must be positive")
    return args


def load_env_files() -> None:
    for filename in (".env.local", ".env"):
        path = REPO_ROOT / filename
        if not path.exists():
            continue
        for raw_line in path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key:
                os.environ.setdefault(key, value)


def read_notebook(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        notebook = json.load(handle)
    if not isinstance(notebook.get("cells"), list):
        raise ValueError("notebook has no cells list")
    return notebook


def source_text(cell: dict[str, Any]) -> str:
    source = cell.get("source", "")
    return source if isinstance(source, str) else "".join(source)


def split_long_text(text: str, max_chars: int) -> list[str]:
    if len(text) <= max_chars:
        return [text]
    pieces = re.split(r"(?<=\n)", text)
    chunks: list[str] = []
    current = ""
    for piece in pieces:
        if len(piece) > max_chars:
            if current:
                chunks.append(current)
                current = ""
            chunks.extend(piece[i : i + max_chars] for i in range(0, len(piece), max_chars))
            continue
        if len(current) + len(piece) > max_chars:
            chunks.append(current)
            current = piece
        else:
            current += piece
    if current:
        chunks.append(current)
    return chunks


def make_segments(notebook: dict[str, Any], max_chars: int) -> list[Segment]:
    segments: list[Segment] = []
    for cell_index, cell in enumerate(notebook["cells"]):
        if cell.get("cell_type") != "markdown":
            continue
        text = source_text(cell)
        if not text.strip():
            continue
        parts = split_long_text(text, max_chars)
        for part_index, part in enumerate(parts):
            key = f"{cell_index}:{part_index}" if len(parts) > 1 else str(cell_index)
            digest = hashlib.sha256(
                (SYSTEM_PROMPT + GLOSSARY + f"\nSOURCE\n{part}").encode("utf-8")
            ).hexdigest()
            segments.append(Segment(key=key, text=part, cache_key=digest))
    return segments


def make_batches(segments: list[Segment], max_chars: int, max_segments: int) -> list[list[Segment]]:
    batches: list[list[Segment]] = []
    current: list[Segment] = []
    current_chars = 0
    for segment in segments:
        segment_chars = len(segment.text)
        if current and (
            len(current) >= max_segments
            or current_chars + segment_chars > max_chars
        ):
            batches.append(current)
            current = []
            current_chars = 0
        current.append(segment)
        current_chars += segment_chars
    if current:
        batches.append(current)
    return batches


def extract_json(content: str) -> dict[str, str]:
    content = content.strip()
    if content.startswith("```"):
        content = re.sub(r"^```(?:json)?\s*", "", content)
        content = re.sub(r"\s*```$", "", content)
    start = content.find("{")
    end = content.rfind("}")
    if start < 0 or end <= start:
        raise ValueError("model response does not contain a JSON object")
    parsed = json.loads(content[start : end + 1])
    if not isinstance(parsed, dict):
        raise ValueError("model response is not a JSON object")
    # Some models wrap the flat mapping in a {"segments": {...}} envelope
    # or echo back the full request including "target_language".
    if isinstance(parsed.get("segments"), dict):
        parsed = parsed["segments"]
    translations: dict[str, str] = {}
    for key, value in parsed.items():
        if not isinstance(value, str):
            raise ValueError(f"translation for {key!r} is not a string")
        translations[key] = value
    return translations


def call_api(
    args: argparse.Namespace,
    batch: list[Segment],
    cache: dict[str, str],
) -> dict[str, str]:
    result = {segment.cache_key: cache[segment.cache_key] for segment in batch if segment.cache_key in cache}
    pending = [segment for segment in batch if segment.cache_key not in cache]
    if not pending:
        return result

    payload: dict[str, Any] = {
        "model": args.model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT + GLOSSARY},
            {
                "role": "user",
                "content": json.dumps(
                    {"target_language": "zh-CN", "segments": {s.key: s.text for s in pending}},
                    ensure_ascii=False,
                ),
            },
        ],
        "temperature": args.temperature,
    }
    headers = {
        "Authorization": f"Bearer {args.api_key}",
        "Content-Type": "application/json",
    }

    use_json_mode = True
    last_error: Exception | None = None
    for attempt in range(1, args.retries + 1):
        request_payload = copy.deepcopy(payload)
        if use_json_mode:
            request_payload["response_format"] = {"type": "json_object"}
        try:
            response = requests.post(
                f"{args.base_url.rstrip('/')}/chat/completions",
                headers=headers,
                json=request_payload,
                timeout=args.timeout,
            )
            if response.status_code == 400 and use_json_mode:
                use_json_mode = False
                continue
            if response.status_code == 429:
                try:
                    error = response.json().get("error", {})
                except Exception:
                    error = {}
                if error.get("code") == "1113":
                    raise FatalAPIError("GLM account has insufficient balance or no resource package")
            if response.status_code in (408, 409, 429, 500, 502, 503, 504):
                raise RuntimeError(f"HTTP {response.status_code}: {response.text[:300]}")
            response.raise_for_status()
            body = response.json()
            content = body["choices"][0]["message"]["content"]
            translations = extract_json(content)
            missing = [segment.key for segment in pending if segment.key not in translations]
            if missing:
                raise ValueError(f"model omitted keys: {missing}")
            for segment in pending:
                translation = translations[segment.key]
                cache[segment.cache_key] = translation
                result[segment.cache_key] = translation
            return result
        except Exception as exc:  # noqa: BLE001 - report one clear error per batch
            last_error = exc
            if attempt == args.retries:
                break
            time.sleep(min(2 ** attempt, 30))
    raise RuntimeError(f"translation API failed after {args.retries} attempts: {last_error}")


def load_cache(cache_dir: Path) -> dict[str, str]:
    path = cache_dir / "en-zh.json"
    if not path.exists():
        return {}
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    return value if isinstance(value, dict) else {}


def save_cache(cache_dir: Path, cache: dict[str, str]) -> None:
    cache_dir.mkdir(parents=True, exist_ok=True)
    path = cache_dir / "en-zh.json"
    temporary = path.with_suffix(".json.tmp")
    temporary.write_text(
        json.dumps(cache, ensure_ascii=False, indent=0, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def translated_notebook(
    source: Path,
    notebook: dict[str, Any],
    segments: list[Segment],
    cache: dict[str, str],
) -> dict[str, Any]:
    target = copy.deepcopy(notebook)
    translated_by_cell: dict[int, str] = {}
    for segment in segments:
        if segment.cache_key not in cache:
            raise ValueError(f"missing translation for Markdown cell {segment.key}")
        translated = cache[segment.cache_key]
        cell_index = int(segment.key.split(":", 1)[0])
        translated_by_cell[cell_index] = translated_by_cell.get(cell_index, "") + translated
    for cell_index, text in translated_by_cell.items():
        target["cells"][cell_index]["source"] = text.splitlines(keepends=True)

    markdown_cells = [cell for cell in target["cells"] if cell.get("cell_type") == "markdown"]
    if markdown_cells:
        notice = (
            "> **中文阅读版**：本文件是 "
            f"`{source.name}` 的 Markdown 翻译副本。代码、输出、图表和路径保持原样；"
            "专有名词和标识符保留英文。\n"
        )
        first = markdown_cells[0]["source"]
        first_text = first if isinstance(first, str) else "".join(first)
        markdown_cells[0]["source"] = (notice + first_text).splitlines(keepends=True)
    return target


def verify_notebook(source: dict[str, Any], target: dict[str, Any]) -> None:
    if len(source["cells"]) != len(target["cells"]):
        raise ValueError("cell count changed")
    for index, (old, new) in enumerate(zip(source["cells"], target["cells"])):
        if old.get("cell_type") != new.get("cell_type"):
            raise ValueError(f"cell {index} type changed")
        if old.get("cell_type") != "code":
            continue
        if source_text(old) != source_text(new):
            raise ValueError(f"code cell {index} source changed")
        if old.get("outputs", []) != new.get("outputs", []):
            raise ValueError(f"code cell {index} outputs changed")
        if old.get("execution_count") != new.get("execution_count"):
            raise ValueError(f"code cell {index} execution count changed")
    prose_cells = [
        "".join(cell.get("source", []))
        for cell in target["cells"]
        if cell.get("cell_type") == "markdown"
    ]
    checkable = [text for text in prose_cells if len(text) >= 120]
    chinese_cells = [text for text in checkable if re.search(r"[\u4e00-\u9fff]", text)]
    if checkable and len(chinese_cells) / len(checkable) < 0.8:
        raise ValueError("translated notebook still contains mostly untranslated Markdown")


def translate_notebook(
    source_path: Path,
    args: argparse.Namespace,
    cache: dict[str, str],
) -> tuple[Path, int, int, bool]:
    target_path = source_path.with_suffix(".zh-CN.ipynb")
    if target_path.exists() and not args.overwrite:
        return target_path, 0, 0, True

    notebook = read_notebook(source_path)
    segments = make_segments(notebook, args.max_chars)
    if not segments:
        raise ValueError("notebook has no non-empty Markdown cells")

    if not args.dry_run:
        batches = make_batches(segments, args.max_chars, args.max_segments)
        for batch in batches:
            call_api(args, batch, cache)

    target = translated_notebook(source_path, notebook, segments, cache)
    verify_notebook(notebook, target)
    if not args.dry_run:
        target_path.write_text(
            json.dumps(target, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8",
        )
    source_chars = sum(len(segment.text) for segment in segments)
    cached = sum(segment.cache_key in cache for segment in segments)
    return target_path, source_chars, cached, False


def discover_notebooks(roots: list[str]) -> list[Path]:
    paths: list[Path] = []
    for root_name in roots:
        root = REPO_ROOT / root_name
        if not root.exists():
            raise FileNotFoundError(f"chapter root does not exist: {root}")
        paths.extend(
            path for path in root.rglob("*.ipynb")
            if not path.name.endswith(".zh-CN.ipynb")
            and ".ipynb_checkpoints" not in path.parts
        )
    return sorted(set(paths))


def main() -> int:
    load_env_files()
    args = parse_args()
    roots = args.roots or DEFAULT_ROOTS
    paths = discover_notebooks(roots)
    if args.limit:
        paths = paths[: args.limit]

    stats = Stats()
    cache = load_cache(args.cache_dir)
    print(f"Provider: {args.provider}; model: {args.model}; notebooks: {len(paths)}")
    if args.dry_run:
        print("Dry run: no API calls or notebook files will be written.")

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(translate_notebook, path, args, cache): path
            for path in paths
        }
        fatal_error: FatalAPIError | None = None
        for future in as_completed(futures):
            path = futures[future]
            stats.notebooks += 1
            try:
                target, source_chars, cached_count, skipped = future.result()
                if not args.dry_run:
                    save_cache(args.cache_dir, cache)
                if skipped:
                    stats.skipped += 1
                    print(f"SKIP  {path} -> {target.name}")
                elif args.dry_run:
                    stats.planned += 1
                    print(f"PLAN  {path} -> {target.name} ({source_chars:,} chars)")
                else:
                    stats.translated += 1
                    stats.source_chars += source_chars
                    stats.cached_segments += cached_count
                    stats.api_segments += len(make_segments(read_notebook(path), args.max_chars)) - cached_count
                    print(f"OK    {path} -> {target.name} ({source_chars:,} chars)")
            except Exception as exc:  # noqa: BLE001 - continue other notebooks after failures
                stats.failed += 1
                print(f"FAIL  {path}: {exc}", file=sys.stderr)
                if isinstance(exc, FatalAPIError):
                    fatal_error = exc
                    break

        if fatal_error:
            for future in futures:
                future.cancel()

    if not args.dry_run:
        save_cache(args.cache_dir, cache)

    print(
        "\nSummary: {notebooks} scanned, {translated} translated, "
        "{planned} planned, "
        "{skipped} skipped, {failed} failed; {chars:,} source chars; "
        "segments: {cached:,} cached / {api:,} API".format(
            notebooks=stats.notebooks,
            translated=stats.translated,
            planned=stats.planned,
            skipped=stats.skipped,
            failed=stats.failed,
            chars=stats.source_chars,
            cached=stats.cached_segments,
            api=stats.api_segments,
        )
    )
    return 2 if fatal_error else (1 if stats.failed else 0)


if __name__ == "__main__":
    raise SystemExit(main())
