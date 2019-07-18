from flask import Flask
from flask import request
import categoriser

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/categorise', methods=['POST'])
def categoriser():
    content = request.get_json()
    print(content)
    t1 = co
    return categoriser.getTestVar()


if __name__ == '__main__':
    app.run()
