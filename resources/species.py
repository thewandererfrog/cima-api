from flask import Blueprint
from flask_restful import Resource,Api
import json

from models import Species

class SpeciesList(Resource):
    def get(self,group_id):
        try:
            species = (Species
                            .select()
                            .where(Species.group_id == group_id)
                            .dicts())
            return json.dumps(list(species))
        except:
            return "No records found"    

class SpeciesDetail(Resource):
    def get(self,id):
        try:
            species = Species.select().where(Species.id == id).dicts().get()
            return json.dumps(species)
        except:
            return "No records found"    

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