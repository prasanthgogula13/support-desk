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

## API endpoints

### Create a ticket

```http
POST /tickets
Content-Type: application/json
```

Request body:

```json
{
  "title": "Unable to connect to VPN",
  "description": "Connection fails from home."
}
```

Successful response: `201 Created`

```json
{
  "title": "Unable to connect to VPN",
  "description": "Connection fails from home.",
  "status": "open"
}
```

Missing, blank, or incorrectly typed fields return `422 Unprocessable Content`.

Tickets are not stored yet; database persistence will be added in a later ticket.

## Run the tests

```powershell
python -m pytest -v
```
