# Support Desk API

A Python backend service for managing internal support tickets.

## Requirements

- Python 3.12
- Git

## Setup

Create and activate a virtual environment:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install runtime and development dependencies:

```powershell
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt
```

## Run the API

```powershell
python -m fastapi dev main.py
```

Available URLs:

- Health check: http://127.0.0.1:8000/health
- Interactive API documentation: http://127.0.0.1:8000/docs

## Run the tests

```powershell
python -m pytest -v
```
