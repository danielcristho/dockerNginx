#WS1 SIDE
from flask import Flask

ws1 = Flask(__name__)
@ws1.route('/')

def hello_world():
    return 'Welcome to webserver1'

if __name__ == '__main__':
    ws1.run(debug=True, host='0.0.0.0')

