from flask import Blueprint
from flask_restful import Resource,Api
import json

from models import Packaging

class PackagingList(Resource):
    def get(self):
        try:
            packaging = Packaging.select().dicts()
            print(list(packaging))    
            return json.dumps(list(packaging))
        except:
            return "No records found"    

class PackagingDetail(Resource):
    def get(self,id):
        try:
            packaging = Packaging.select().where(Packaging.id == id).dicts(True).get()
            return json.dumps(packaging)
        except:
            return "No records found"    

# Create a Blueprint for the Resources
packaging_api = Blueprint('resources.packaging',__name__)        
# Create an Api from the Blueprint
api = Api(packaging_api)

# Add resources
api.add_resource(
    PackagingList, '/api/v1/packaging',
    endpoint='packaging'
)

api.add_resource(
    PackagingDetail, '/api/v1/packaging/detail/<int:id>',
    endpoint='packaging_detail'
)