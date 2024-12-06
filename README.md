# Points Tracker API

## Overview
This REST API tracks points for a user, supporting adding, spending, and fetching balances.

## Endpoints
1. `/add` (POST): Add points.
2. `/spend` (POST): Spend points.
3. `/balance` (GET): Get balance.

## Installation
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the server: `python app.py`.

## Testing
Run tests using `python -m unittest tests.py`.

## Example Usage
1. Add points: `curl -X POST -H "Content-Type: application/json" -d '{"payer": "DANNON", "points": 300, "timestamp": "2022-10-31T10:00:00Z"}' http://127.0.0.1:8000/add`
2. Get balance: `curl http://127.0.0.1:8000/balance`
3. Spend points: `curl -X POST -H "Content-Type: application/json" -d '{"points": 500}' http://127.0.0.1:8000/spend`
