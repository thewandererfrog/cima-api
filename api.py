from flask import Flask

from database import initialize
from resources.groups import groups_api
from resources.species import species_api

DEBUG = True
HOST = '0.0.0.0'
PORT = 8080

app = Flask(__name__)

app.register_blueprint(groups_api)
app.register_blueprint(species_api)

@app.route('/')
def hello_world():
    return 'Hello'

if __name__ == '__main__':
    initialize()
    app.run(debug=DEBUG,host=HOST,port=PORT)        