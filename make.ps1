param(
    [Parameter(Mandatory)]
    [string]$TARGET,

    [Parameter()]
    [string]$GOAL,

    [Parameter()]
    [int]$COUNT = 100
)
$ErrorActionPreference = 'Continue'
$VIRTUAL_ENV = "venv"

function Get-Python-Version {
    try {
        $pythonVersion = python --version
        $pythonVersion.Split()[1]
    }
    catch {
        Write-Error "Failed to get python version.  Is python installed?" -ErrorAction Stop
    }
}


function Check-Python-Version {
    $version = Get-Python-Version
    if ([Version]$version -lt [Version]"3.8") {
        Write-Error "Invalid version of python: ${version}. Must be 3.8+" -ErrorAction Stop
    }
}

function Make-Venv {
    Check-Python-Version
    if (!(Test-Path -Path "venv\Scripts\activate")) {
        Write-Host "Creating virtual environment..."
        python -m venv $VIRTUAL_ENV
    }
}

function Activate-Venv {
    Make-Venv
    .\venv\Scripts\activate
}


function Run-In-Env($runCmd) {
    Activate-Venv
    $env:PYTHONPATH='.'
    Invoke-Expression $runCmd
}


function Run-App($appArgs) {
    Run-In-Env "python src\functions\handler.py $appArgs"
}

function Make($target) {
    switch ($target) {
        "init" {
            Activate-Venv
            pip install -r requirements.txt
        }
        "run" {
            Run-App "--goal $GOAL"
        }
        "evaluate" {
            Run-App "--evaluate $COUNT"
        }
        "test" {
            Run-In-Env "pytest tests"
        }
        "lint" {
            Run-In-Env "flake8 src tests"
            Run-In-Env "mypy src tests"
        }
        "check" {
            Make lint
            Make test
        }
    }
}

Make $TARGET
