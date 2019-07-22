from flask import Flask
from flask import request
from flask import make_response
from flask import jsonify
from transaction import transaction_from_json
from categoriser import transaction_similarities
from transactor_service import get_transactions_in_last_month_by_user_id
from transactor_service import update_category_of_transactions
from constants import USER_ID_HEADER
import numpy as np

app = Flask(__name__)

THRESHOLD = 0.9


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    health = {"status": "healthy"}
    return make_response(jsonify(health), 200)


# Header: USER_ID_HEADER('x-n26-userid') (required)
# Body: JSON Transaction
@app.route('/find-similar-transactions', methods=['POST'])
def find_similar_trnasactions_for_user():
    content = request.get_json()
    user_id = request.headers[USER_ID_HEADER]
    transaction = transaction_from_json(content)
    transactions, transactions_json = get_transactions_in_last_month_by_user_id(user_id)
    similarities = transaction_similarities(transaction, transactions)
    indices = np.where(similarities > THRESHOLD)[0]
    result = []
    for index in indices:
        if transactions[index].id != transaction.id:
            result.append(transactions_json[index])
    return make_response(jsonify(result), 200)


# URL param: category id
# Header: USER_ID_HEADER('x-n26-userid') (required)
# Body: JSON list of Transaction
@app.route('/update-categories/<category_id>', methods=['PUT'])
def update_categories(category_id):
    content = request.get_json()
    user_id = request.headers[USER_ID_HEADER]
    transactions = []
    for tx in content:
        transactions.append(transaction_from_json(tx))
    update_category_of_transactions(category_id, transactions, user_id)
    return make_response(jsonify(), 201)


if __name__ == '__main__':
    app.run()
