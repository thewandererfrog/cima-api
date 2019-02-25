from flask import Blueprint
from flask_restful import Resource,Api,reqparse
import json

from models import Product

class ProductList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('group_id',required=True,type=int,location='args')
        self.reqparse.add_argument('species_id',required=True,type=int,location='args')
        self.reqparse.add_argument('variety_id',type=int,location='args')
        self.reqparse.add_argument('category_id',type=int,location='args')
        self.reqparse.add_argument('caliber_id',type=int,location='args')
        self.reqparse.add_argument('packaging_id',type=int,location='args')
        super().__init__()

    def get(self):
        args = self.reqparse.parse_args()
        expression = (Product.group_id == args['group_id']) & (Product.species_id == args['species_id'])
        # clean unecessary args
        del args['group_id']
        del args['species_id']
        # build where clause based on qeury params
        for key,value in args.items():
            print(key,value)
            if value is not None:
                expression &= (getattr(Product,key) == value)

        try:
            products = (
                Product
                .select()
                .where(
                    expression
                )
                .dicts()
            )   
            print(list(products))
            return json.dumps(list(products), sort_keys=True, default=str)
        except Exception as e: 
            print(e)
            return "Bad request"

# Create a Blueprint for the Resources
products_api = Blueprint('resources.products',__name__)        
# Create an Api from the Blueprint
api = Api(products_api)

# Add resources
api.add_resource(
    ProductList, '/api/v1/products',
    endpoint='products'
)