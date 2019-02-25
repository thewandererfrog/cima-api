from flask import Blueprint
from flask_restful import Resource,Api,marshal,marshal_with,fields,abort
import json

from models import Variety

variety_field = {
    'id' : fields.Integer,
    'name' : fields.String
}

class VarietyList(Resource):

    def get(self,species_id):
        try:
            varieties = [marshal(variety,variety_field) 
                            for variety in (Variety
                                .select()
                                .where(Variety.species_id == species_id)
                            )
                        ]
        except Exception as e:
            print(e)
            abort(400,message="Something went wrong")  
        else:
            return { 'varieties' : varieties }

            
class VarietyDetail(Resource):
    def get(self,id):
        try:
            variety = Variety.select().where(Variety.id == id).dicts().get()
            return json.dumps(variety)
        except:
            return "No records found"    

# Create a Blueprint for the Resources
varieties_api = Blueprint('resources.varieties',__name__)        
# Create an Api from the Blueprint
api = Api(varieties_api)

# Add resources
api.add_resource(
    VarietyList, '/api/v1/varieties/<int:species_id>',
    endpoint='varieties'
)

api.add_resource(
    VarietyDetail, '/api/v1/variety/detail/<int:id>',
    endpoint='variety_detail'
)