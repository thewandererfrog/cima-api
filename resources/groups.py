from flask import Blueprint
from flask_restful import Resource,Api
import json

from models import Group

class GroupList(Resource):
    def get(self):
        try:
            groups = Group.select().dicts()
            print(list(groups))    
            return json.dumps(list(groups))
        except:
            return "No records found"    

class GroupDetail(Resource):
    def get(self,id):
        try:
            group = Group.select().where(Group.id == id).dicts(True).get()
            return json.dumps(group)
        except:
            return "No records found"    

# Create a Blueprint for the Resources
groups_api = Blueprint('resources.groups',__name__)        
# Create an Api from the Blueprint
api = Api(groups_api)

# Add resources
api.add_resource(
    GroupList, '/api/v1/groups',
    endpoint='groups'
)

api.add_resource(
    GroupDetail, '/api/v1/groups/detail/<int:id>',
    endpoint='group'
)