from flask import Blueprint
from flask_restful import Resource,Api
import json

from models import Caliber

class CaliberList(Resource):
    def get(self):
        try:
            calibers = Caliber.select().dicts()
            print(list(calibers))    
            return json.dumps(list(calibers))
        except:
            return "No records found"    

class CaliberDetail(Resource):
    def get(self,id):
        try:
            caliber = Caliber.select().where(Caliber.id == id).dicts(True).get()
            return json.dumps(caliber)
        except:
            return "No records found"    

# Create a Blueprint for the Resources
calibers_api = Blueprint('resources.calibers',__name__)        
# Create an Api from the Blueprint
api = Api(calibers_api)

# Add resources
api.add_resource(
    CaliberList, '/api/v1/calibers',
    endpoint='calibers'
)

api.add_resource(
    CaliberDetail, '/api/v1/calibers/detail/<int:id>',
    endpoint='caliber'
)