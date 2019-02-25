from flask import Blueprint
from flask_restful import Resource,Api
import json

from models import Category

class CategoryList(Resource):
    def get(self,variety_id):
        try:
            categories = (Category
                            .select()
                            .where(Category.variety_id == variety_id)
                            .dicts())
            return json.dumps(list(categories))
        except:
            return "No records found"    

class CategoryDetail(Resource):
    def get(self,id):
        try:
            category = Category.select().where(Category.id == id).dicts().get()
            return json.dumps(category)
        except:
            return "No records found"    

# Create a Blueprint for the Resources
categories_api = Blueprint('resources.categories',__name__)        
# Create an Api from the Blueprint
api = Api(categories_api)

# Add resources
api.add_resource(
    CategoryList, '/api/v1/categories/<int:variety_id>',
    endpoint='categories'
)

api.add_resource(
    CategoryDetail, '/api/v1/category/detail/<int:id>',
    endpoint='category_detail'
)