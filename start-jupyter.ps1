$ErrorActionPreference = "Stop"

$repoRoot = $PSScriptRoot
$env:ML4T_DATA_PATH = Join-Path $repoRoot "data"
$env:EDGAR_LOCAL_DATA_DIR = Join-Path $repoRoot ".edgar"
$env:EDGAR_CACHE_DIR = Join-Path $repoRoot ".edgar_cache"

& (Join-Path $repoRoot ".venv\Scripts\python.exe") -m jupyter lab
