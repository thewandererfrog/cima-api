from flask import Blueprint
from flask_restful import Resource,Api,marshal,marshal_with,fields,abort
import json

from models import Product,Variety

variety_fields = {
    'id' : fields.Integer,
    'name' : fields.String
}

class VarietyList(Resource):

    def get(self,species_id):
        try:
            varieties = [marshal(variety,variety_fields) 
                            for variety in (
                                Product
                                    .select(Product.variety_id.alias('id'),Variety.name)
                                    .join(Variety, on=(Product.variety_id == Variety.id))
                                    .where(Product.species_id == species_id)
                                    .distinct().dicts()
                                )
                        ]
        except Exception as e:
            print(e)
            abort(400,message="Something went wrong")  
        else:
            # return json.dumps(list(product.dicts()))
            return { 'varieties' : varieties }


class VarietyDetail(Resource):
    @marshal_with(variety_fields)
    def get(self,id):
        try:
            variety = Variety.get(Variety.id == id)
        except Exception as e:
            print(e)
            abort(400,message="Something went wrong")  
        else:
            return variety

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