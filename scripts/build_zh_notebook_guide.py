from __future__ import annotations

import json
from pathlib import Path


CHAPTER_TITLES = {
    "01_process_is_edge": "第 1 章：流程就是你的优势",
    "02_financial_data_universe": "第 2 章：金融数据全景",
    "03_market_microstructure": "第 3 章：市场微观结构",
    "04_fundamental_alternative_data": "第 4 章：基本面与另类数据",
    "05_synthetic_data": "第 5 章：合成金融数据",
    "06_strategy_definition": "第 6 章：策略研究框架",
    "07_defining_the_learning_task": "第 7 章：定义学习任务",
    "08_financial_features": "第 8 章：金融特征工程",
    "09_model_based_features": "第 9 章：基于模型的特征提取",
    "10_text_feature_engineering": "第 10 章：文本特征工程",
    "11_ml_pipeline": "第 11 章：机器学习流水线",
    "12_gradient_boosting": "第 12 章：梯度提升与高级表格模型",
    "13_dl_time_series": "第 13 章：深度学习时间序列",
    "14_latent_factors": "第 14 章：潜因子模型",
    "15_causal_estimation": "第 15 章：因果机器学习",
    "16_strategy_simulation": "第 16 章：策略模拟",
    "17_portfolio_construction": "第 17 章：组合构建",
    "18_transaction_costs": "第 18 章：交易成本",
    "19_risk_management": "第 19 章：风险管理",
    "20_strategy_synthesis": "第 20 章：策略合成",
    "21_rl_execution_hedging": "第 21 章：用于执行与对冲的强化学习",
    "22_rag_financial_research": "第 22 章：金融研究中的 RAG",
    "23_knowledge_graphs": "第 23 章：知识图谱",
    "24_autonomous_agents": "第 24 章：自治智能体",
    "25_live_trading": "第 25 章：实盘交易系统",
    "26_mlops_governance": "第 26 章：MLOps 与治理",
}

CASE_STUDY_TITLES = {
    "cme_futures": "案例研究：CME 期货",
    "crypto_perps_funding": "案例研究：加密货币永续合约资金费率",
    "etfs": "案例研究：ETF",
    "fx_pairs": "案例研究：外汇货币对",
    "nasdaq100_microstructure": "案例研究：NASDAQ-100 微观结构",
    "sp500_equity_option_analytics": "案例研究：S&P 500 股票与期权分析",
    "sp500_options": "案例研究：S&P 500 期权",
    "us_equities_panel": "案例研究：美国股票面板",
    "us_firm_characteristics": "案例研究：美国公司特征",
}


def notebook_title(path: Path) -> tuple[str, int]:
    try:
        with path.open(encoding="utf-8") as handle:
            document = json.load(handle)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return path.stem.replace("_", " "), 0

    markdown_cells = [
        cell for cell in document.get("cells", []) if cell.get("cell_type") == "markdown"
    ]
    for cell in markdown_cells:
        source = "".join(cell.get("source", []))
        for line in source.splitlines():
            stripped = line.strip()
            if stripped.startswith("#"):
                return stripped.lstrip("#").strip(), len(markdown_cells)
        if source.strip():
            return source.strip().splitlines()[0], len(markdown_cells)
    return path.stem.replace("_", " "), len(markdown_cells)


def escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def source_notebooks(directory: Path) -> list[Path]:
    return [
        path
        for path in sorted(directory.rglob("*.ipynb"))
        if not path.name.endswith(".zh-CN.ipynb")
    ]


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    output = root / "docs" / "zh-CN" / "notebook-guide.md"
    output.parent.mkdir(parents=True, exist_ok=True)

    sections: list[str] = []
    total_notebooks = 0
    total_markdown = 0

    sections_by_key: dict[str, list[str]] = {}
    directories: list[tuple[str, Path, dict[str, str]]] = []
    for directory in sorted(path for path in root.iterdir() if path.is_dir()):
        if directory.name in CHAPTER_TITLES:
            directories.append((directory.name, directory, CHAPTER_TITLES))

    case_root = root / "case_studies"
    if case_root.exists():
        for directory in sorted(path for path in case_root.iterdir() if path.is_dir()):
            title = CASE_STUDY_TITLES.get(
                directory.name, f"案例研究：{directory.name.replace('_', ' ')}"
            )
            directories.append((directory.name, directory, {directory.name: title}))

    for section_key, directory, titles in directories:
        notebooks = source_notebooks(directory)
        if not notebooks:
            continue

        rows: list[str] = []
        chapter_markdown = 0
        for notebook in notebooks:
            title, markdown_count = notebook_title(notebook)
            chapter_markdown += markdown_count
            relative = f"../../{notebook.relative_to(root).as_posix()}"
            chinese = notebook.with_name(notebook.stem + ".zh-CN.ipynb")
            chinese_link = (
                f"[中文版](../../{chinese.relative_to(root).as_posix()})"
                if chinese.exists()
                else "未翻译"
            )
            rows.append(
                f"| [{notebook.name}]({relative}) | {escape(title)} | {chinese_link} | {markdown_count} |"
            )

        total_notebooks += len(notebooks)
        total_markdown += chapter_markdown
        chapter_title = titles[section_key]
        relative_readme = (
            f"../../{directory.relative_to(root).as_posix()}/README.md"
        )
        sections_by_key[chapter_title] = (
            "\n".join(
                [
                    f"## {chapter_title}",
                    "",
                    f"共 {len(notebooks)} 个 notebook，{chapter_markdown} 个 Markdown 说明 cell。",
                    "",
                    "| Notebook | 原标题 | 中文版 | 说明 cell |",
                    "|---|---|---|---: |",
                    *rows,
                    "",
                    f"章节说明见 [`{directory.relative_to(root).as_posix()}/README.md`]({relative_readme})。",
                    "",
                ]
            )
        )

    data_notebooks = source_notebooks(root / "data")
    if data_notebooks:
        rows = []
        data_markdown = 0
        for notebook in data_notebooks:
            title, markdown_count = notebook_title(notebook)
            data_markdown += markdown_count
            relative = f"../../{notebook.relative_to(root).as_posix()}"
            rows.append(
                f"| [{notebook.relative_to(root / 'data').as_posix()}]({relative}) | {escape(title)} | 未翻译 | {markdown_count} |"
            )
        total_notebooks += len(data_notebooks)
        total_markdown += data_markdown
        sections_by_key["数据集说明 notebook"] = "\n".join(
            [
                "## 数据集说明 notebook",
                "",
                f"共 {len(data_notebooks)} 个 notebook，{data_markdown} 个 Markdown 说明 cell。",
                "",
                "| Notebook | 原标题 | 中文版 | 说明 cell |",
                "|---|---|---|---: |",
                *rows,
                "",
                "数据源、授权和下载细节见 [`data/README.md`](../../data/README.md)。",
                "",
            ]
        )

    sections = [sections_by_key[title] for title in sections_by_key]

    guide = "\n".join(
        [
            "# Notebook 中文导览",
            "",
            "这份索引覆盖当前仓库的全部 Jupyter notebook，帮助你先判断每个文件在整本书工作流中的位置，再决定是否打开或翻译。",
            "",
            f"- Notebook 总数：**{total_notebooks}**",
            f"- Markdown 说明 cell 总数：**{total_markdown}**",
            "- 原始 notebook 保持不变；代码、输出、图表和路径都以原文件为准。",
            "- 链接从本文件跳到对应 notebook；`说明 cell` 数量越大，通常叙述内容越多。",
            "",
            "## 阅读方式",
            "",
            "1. 先读章节 `README.md`，确认章节目标和小节结构。",
            "2. 再从下表选择 notebook。文件名通常按章节内顺序排列，`00_` 多为导入与基础概念。",
            "3. 打开 notebook 后，优先看 Markdown 标题、导入库、配置参数和最后的结论 cell。",
            "4. 如果只想运行，不改代码，从仓库根目录按章节 README 的命令执行。",
            "",
            "---",
            "",
            *sections,
            "---",
            "",
            "## 翻译约定",
            "",
            "- 代码、库名、函数名、参数名、文件路径和环境变量不翻译。",
            "- `walk-forward validation` 译为“walk-forward 验证”，保留英文原词以便检索。",
            "- `regime` 视上下文译为“市场状态 / regime”。",
            "- `leakage` 译为“数据泄漏”，`lookahead bias` 译为“前视偏差”。",
            "- 模型名、数据集名和机构名保留英文。",
            "",
        ]
    )

    output.write_text(guide, encoding="utf-8", newline="\n")
    print(f"Wrote {output} with {total_notebooks} notebooks")


if __name__ == "__main__":
    main()
