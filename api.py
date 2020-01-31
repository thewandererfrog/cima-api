from flask import Flask
from flask_cors import CORS
from database import initialize
import os

# Import Blueprints
import resources

# Database config
DEBUG = True
HOST = '0.0.0.0'
PORT = os.getenv('PORT')

app = Flask(__name__)
CORS(app)

# Register blueprints
app.register_blueprint(resources.groups_api)
app.register_blueprint(resources.species_api)
app.register_blueprint(resources.varieties_api)
app.register_blueprint(resources.categories_api)
app.register_blueprint(resources.markets_api)
app.register_blueprint(resources.regions_api)
app.register_blueprint(resources.calibers_api)
app.register_blueprint(resources.packaging_api)
app.register_blueprint(resources.products_api)

# Test endpoint
@app.route('/healthy')
def healthy():
    return 'OK'

if __name__ == '__main__':
    initialize()
    app.run(debug=DEBUG,host=HOST,port=PORT)        