from flask import Blueprint
from flask_restful import Resource,Api,marshal,marshal_with,fields,abort,reqparse
import json

from models import Category,Product

category_fields = {
    'id' : fields.Integer,
    'name' : fields.String
}

class CategoryList(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('species_id',required=True,type=int,location='args')
        self.reqparse.add_argument('variety_id',type=int,location='args')
        super().__init__()

    def get(self):
        args = self.reqparse.parse_args()
        expression = (Product.species_id == args['species_id'])

        # build where clause based on qeury params
        for key,value in args.items():
            if value is not None:
                expression &= (getattr(Product,key) == value)

        try:
            categories = [marshal(category,category_fields) 
                            for category in (
                                Product
                                    .select(Product.category.alias('id'),Category.name)
                                    .join(Category, on=(Product.category == Category.id))
                                    .where(expression)
                                    .distinct().dicts()
                                )
                        ]
        except Exception as e:
            abort(400,message="Something went wrong")  
        else:
            return { 'categories' : categories}

class CategoryDetail(Resource):
    @marshal_with(category_fields)
    def get(self,id):
        try:
            category = Category.get(Category.id == id)
        except Exception as e:
            print(e)
            abort(404,message="Something went wrong")  
        else:
            return category

# Create a Blueprint for the Resources
categories_api = Blueprint('resources.categories',__name__)        
# Create an Api from the Blueprint
api = Api(categories_api)

# Add resources
api.add_resource(
    CategoryList, '/api/v1/categories',
    endpoint='categories'
)

api.add_resource(
    CategoryDetail, '/api/v1/category/detail/<int:id>',
    endpoint='category_detail'
)