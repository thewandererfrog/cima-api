from flask import Blueprint
from flask_restful import Resource,Api,fields,marshal,marshal_with,abort,reqparse
import json

from models import Caliber,Product

caliber_fields = {
    'id' : fields.Integer,
    'name' : fields.String
}

class CaliberList(Resource):
    # Initiate parser
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('species_id',required=True,type=int,location='args')
        self.reqparse.add_argument('variety_id',type=int,location='args')
        self.reqparse.add_argument('category_id',type=int,location='args')
        self.reqparse.add_argument('packaging_id',type=int,location='args')
        super().__init__()

    def get(self):
        # get arguments
        args = self.reqparse.parse_args()
        # Start where clause expression
        expression = (Product.species_id == args['species_id'])

        # build where clause based on qeury params
        for key,value in args.items():
            if value is not None:
                expression &= (getattr(Product,key) == value)

        try:
            # Get from DB
            calibers = [marshal(caliber,caliber_fields) 
                            for caliber in (
                                Product
                                    .select(Product.caliber.alias('id'),Caliber.name)
                                    .join(Caliber, on=(Product.caliber == Caliber.id))
                                    .where(expression)
                                    .distinct().dicts()
                                )
                        ]
        except Exception as e:
            print(e)
            abort(400,message="Something went wrong")  
        else:
            return { 'calibers' : calibers}

class CaliberDetail(Resource):

    @marshal_with(caliber_fields)
    def get(self,id):
        try:
            caliber = Caliber.get(Caliber.id == id)
        except Exception as e:
            print(e)
            abort(404,message="Not found")
        else:
            return caliber    

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