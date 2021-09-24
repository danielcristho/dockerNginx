#WS1 SIDE
from flask import Flask

ws2 = Flask(__name__)
@ws2.route('/')

def hello_world():
    return 'Welcome to webserver2'

if __name__ == '__main__':
    ws2.run(debug=True, host='0.0.0.0')