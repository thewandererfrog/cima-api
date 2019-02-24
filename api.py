from flask import Flask
from database import initialize

DEBUG = True
HOST = '0.0.0.0'
PORT = 8080

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello'

if __name__ == '__main__':
    initialize()
    app.run(debug=DEBUG,host=HOST,port=PORT)        