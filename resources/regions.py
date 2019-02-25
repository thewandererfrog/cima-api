from flask import Blueprint
from flask_restful import Resource,Api
import json

from models import Region

class RegionList(Resource):
    def get(self):
        try:
            regions = Region.select().dicts()
            print(list(regions))    
            return json.dumps(list(regions))
        except:
            return "No records found"    

class RegionDetail(Resource):
    def get(self,id):
        try:
            region = Region.select().where(Region.id == id).dicts(True).get()
            return json.dumps(region)
        except:
            return "No records found"    

# Create a Blueprint for the Resources
regions_api = Blueprint('resources.regions',__name__)        
# Create an Api from the Blueprint
api = Api(regions_api)

# Add resources
api.add_resource(
    RegionList, '/api/v1/regions',
    endpoint='regions'
)

api.add_resource(
    RegionDetail, '/api/v1/regions/detail/<int:id>',
    endpoint='region'
)