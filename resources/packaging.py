from flask import Blueprint
from flask_restful import Resource,Api,marshal,marshal_with,fields,abort,reqparse
import json

from models import Packaging,Product

packaging_fields = {
    'id' : fields.Integer,
    'name' : fields.String
}

class PackagingList(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('species_id',required=True,type=int,location='args')
        self.reqparse.add_argument('variety_id',type=int,location='args')
        self.reqparse.add_argument('category_id',type=int,location='args')
        self.reqparse.add_argument('caliber_id',type=int,location='args')
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
            packaging = [marshal(package,packaging_fields) 
                            for package in (
                                Product
                                    .select(Product.packaging.alias('id'),Packaging.name)
                                    .join(Packaging, on=(Product.packaging == Packaging.id))
                                    .where(expression)
                                    .distinct().dicts()
                                )
                        ]
        except Exception as e:
            print(e)
            abort(400,message="Something went wrong")  
        else:
            return { 'packaging' : packaging}

class PackagingDetail(Resource):

    @marshal_with(packaging_fields)
    def get(self,id):
        try:
            packaging = Packaging.get(Packaging.id == id)
        except Exception as e:
            print(e)
            abort(404,message="Not found")
        else:
            return packaging   

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