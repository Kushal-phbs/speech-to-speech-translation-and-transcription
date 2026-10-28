param(
    [switch]$SkipCreateVenv
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot
$venvDir = Join-Path $repoRoot ".venv"
$venvPython = Join-Path $venvDir "Scripts\python.exe"

Write-Host "Setting up the Python 3.11 environment..."

$python = Get-Command py -ErrorAction SilentlyContinue
if ($python) {
    & py -3.11 --version
    if ($LASTEXITCODE -ne 0) {
        throw "Python 3.11 is required. Install it and ensure 'py -3.11' works."
    }
} else {
    $python = Get-Command python -ErrorAction SilentlyContinue
    if (-not $python) {
        throw "Python 3.11 is required, but neither 'py' nor 'python' was found."
    }
    & python --version
    if ($LASTEXITCODE -ne 0 -or -not (& python -c "import sys; raise SystemExit(0 if sys.version_info[:2] == (3, 11) else 1)")) {
        throw "Python 3.11 is required. Activate or install a Python 3.11 interpreter."
    }
}

if (-not $SkipCreateVenv -and -not (Test-Path $venvPython)) {
    if ($python.Name -like "py*") {
        & py -3.11 -m venv $venvDir
    } else {
        & python -m venv $venvDir
    }
}

if (-not (Test-Path $venvPython)) {
    throw "Virtual environment Python was not created at $venvPython"
}

& $venvPython -m pip install --upgrade pip
& $venvPython -m pip install -r (Join-Path $repoRoot "requirements-dev.txt")

Write-Host ""
Write-Host "Backend environment ready."
Write-Host "Activate it with:"
Write-Host "  .\.venv\Scripts\Activate.ps1"
Write-Host "Run tests with:"
Write-Host "  python -m pytest"
