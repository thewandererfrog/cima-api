from flask import Blueprint
from flask_restful import Resource,Api,marshal,marshal_with,fields,abort
import json

from models import Species

# Output data
species_fields = {
    'id' : fields.Integer,
    'name' : fields.String,
    'group_id' : fields.Integer
}

class SpeciesList(Resource):

    def get(self,group_id):
        try:
            species = [marshal(sp,species_fields) for sp in Species.select().where(Species.group_id == group_id).dicts()]
        except Exception as e:
            print(e)
            abort(400,message="Something went wrong.")
        else:
            return { 'species' : species }    
            # return None

class SpeciesDetail(Resource):

    @marshal_with(species_fields)
    def get(self,id):
        try:
            species = Species.get(Species.id == id)
        except Exception as e:
            print(e)
            abort(404,message="Species not found.")
        else:
            return species    

# Create a Blueprint for the Resources
species_api = Blueprint('resources.species',__name__)        
# Create an Api from the Blueprint
api = Api(species_api)

# Add resources
api.add_resource(
    SpeciesList, '/api/v1/species/<int:group_id>',
    endpoint='species'
)

api.add_resource(
    SpeciesDetail, '/api/v1/species/detail/<int:id>',
    endpoint='species_detail'
)