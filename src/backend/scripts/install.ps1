$ErrorActionPreference = "Stop"

if (-not (Test-Path ".venv")) {
    python -m venv .venv
}

.\.venv\Scripts\python.exe -m pip install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/
.\.venv\Scripts\python.exe -m pip install -e ".[dev]" -i https://mirrors.aliyun.com/pypi/simple/
