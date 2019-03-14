from flask import Blueprint
from flask_restful import Resource,Api,marshal,fields,abort,reqparse
import json
from peewee import fn

from models import Product

product_fields = {
    'date' : fields.DateTime(dt_format='iso8601'),
    'min' : fields.Float,
    'max' : fields.Float,
    'mean' : fields.Float
}


class ProductList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('species_id',required=True,type=int,location='args')
        self.reqparse.add_argument('variety_id',type=int,location='args')
        self.reqparse.add_argument('category_id',type=int,location='args')
        self.reqparse.add_argument('caliber_id',type=int,location='args')
        self.reqparse.add_argument('packaging_id',type=int,location='args')
        self.reqparse.add_argument('region',type=int,location='args')
        self.reqparse.add_argument('from',required=True,location='args')
        self.reqparse.add_argument('to',required=True,location='args')
        super().__init__()

    def get(self):
        args = self.reqparse.parse_args()
        expression = ((Product.species_id == args['species_id']) & (Product.date >= args['from']) & (Product.date <= args['to'])) 
        # clean unecessary args
        del args['species_id']
        del args['from']
        del args['to']
        # build where clause based on qeury params
        for key,value in args.items():
            if value is not None:
                expression &= (getattr(Product,key) == value)

        try:
            products = [marshal(product,product_fields) 
                            for product in (
                                Product
                                    .select(
                                        Product.date,
                                        fn.AVG(Product.min).alias('min'),
                                        fn.AVG(Product.max).alias('max'),
                                        fn.AVG(Product.mean).alias('mean')
                                    )
                                    .where(expression)
                                    .group_by(Product.date)
                                    .order_by(Product.date)
                                    .dicts()
                            )
                        ]   
        except Exception as e: 
            print(e)
            abort(400,message="Something went wrong")  
        else:
            return { 'products' : products }    

# Create a Blueprint for the Resources
products_api = Blueprint('resources.products',__name__)        
# Create an Api from the Blueprint
api = Api(products_api)

# Add resources
api.add_resource(
    ProductList, '/api/v1/products',
    endpoint='products'
)