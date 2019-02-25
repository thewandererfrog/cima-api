from flask import Blueprint
from flask_restful import Resource,Api,abort,fields,marshal_with,marshal
import json

from models import Group

# Output data
group_fields = {
    'id' : fields.Integer,
    'name' : fields.String
}

class GroupList(Resource):

    def get(self):
        try:
            groups = [ marshal(group, group_fields) for group in Group.select() ]
        except Exception as e:
            print(e)
            abort(500,message="Something wrong happened trying to retrieve the groups list.")    
        else:
            return { 'groups' : groups }

class GroupDetail(Resource):
    
    @marshal_with(group_fields)
    def get(self,id):
        try:
            group = Group.get(Group.id == id)
        except Exception as e:
            print(e)
            abort(404,message="Group not found")
        else:
            return group
            
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