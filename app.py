from flask import Flask
from flask import request
from categoriser import transaction_from_json
from categoriser import transaction_similarity

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/categorise', methods=['POST'])
def categoriser():
    content = request.get_json()
    t1 = transaction_from_json(content[0])
    t2 = transaction_from_json(content[1])
    return str(transaction_similarity(t1, t2)[0])


if __name__ == '__main__':
    app.run()
