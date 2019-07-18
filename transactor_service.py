import requests
from datetime import datetime
from transaction import transaction_from_json
from constants import USER_ID_HEADER

transactor_url = "http://transactor.service.consul"
get_all_transactions = "/internal/transactions/all/filter"


def get_transactions_in_last_month_by_user_id(user_id):
    response = requests.get(
        transactor_url + get_all_transactions,
        params={'from': str(get_time_from_start_of_month()),
                'to': str(get_current_time())},
        headers={USER_ID_HEADER: user_id}
    )

    json_response = response.json()
    transactions = []
    for transaction in json_response:
        transactions.append(transaction_from_json(transaction))
    return transactions, json_response


def update_category_of_transactions(category_id, transactions, user_id):
    for tx in transactions:
        requests.put(
            transactor_url + "/internal/transactions/"+tx.id+"/categories/"+category_id,
            headers={USER_ID_HEADER: user_id}
        )
    return 0


def get_current_time():
    return time_to_epoch_milli(datetime.now().timestamp())


def get_time_from_start_of_month():
    today = datetime.today()
    datem = datetime(today.year, today.month, 1)
    return time_to_epoch_milli(datem.timestamp())


def time_to_epoch_milli(time_to_convert):
    return int(round(time_to_convert * 1000))