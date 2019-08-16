from flask import Flask
from  flask import jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify(mohamed='fouad'),200

def hello_world():
    return jsonify(mohamed='fouad'),200

if __name__ == '__main__':
    app.run()
