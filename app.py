from flask import Flask, request, jsonify
from datetime import datetime
from collections import defaultdict

app = Flask(__name__)

# Global variables to store transactions and balances
transactions = []
balances = defaultdict(int)

@app.route('/add', methods=['POST'])
def add_points():
    data = request.get_json()
    payer = data.get('payer')
    points = data.get('points')
    timestamp = data.get('timestamp')

    if not (payer and isinstance(points, int) and timestamp):
        return "Invalid input", 400

    transactions.append({'payer': payer, 'points': points, 'timestamp': datetime.fromisoformat(timestamp[:-1])})
    balances[payer] += points
    return '', 200


@app.route('/spend', methods=['POST'])
def spend_points():
    data = request.get_json()
    points_to_spend = data.get('points')

    if not isinstance(points_to_spend, int):
        return "Invalid input", 400

    total_points = sum(balances.values())
    if points_to_spend > total_points:
        return "Not enough points", 400

    transactions.sort(key=lambda x: x['timestamp'])
    spent_points = []
    for transaction in transactions:
        if points_to_spend <= 0:
            break

        payer = transaction['payer']
        available_points = min(points_to_spend, transaction['points'])

        if balances[payer] + available_points >= 0:  # Prevent payer's balance going negative
            balances[payer] -= available_points
            points_to_spend -= available_points
            spent_points.append({'payer': payer, 'points': -available_points})

    return jsonify(spent_points), 200


@app.route('/balance', methods=['GET'])
def get_balance():
    print(balances)
    return jsonify(balances), 200


if __name__ == '__main__':
    app.run(port=8000)
