from flask import Blueprint
from flask_restful import Resource,Api,marshal,marshal_with,fields,abort,reqparse
import json

from models import Region,Product

region_fields = {
    'id' : fields.Integer,
    'name' : fields.String
}

class RegionList(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('species_id',required=True,type=int,location='args')
        self.reqparse.add_argument('variety_id',type=int,location='args')
        self.reqparse.add_argument('category_id',type=int,location='args')
        self.reqparse.add_argument('packaging_id',type=int,location='args')
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
            regions = [marshal(region,region_fields) 
                            for region in (
                                Product
                                    .select(Product.region_id.alias('id'),Region.name)
                                    .join(Region, on=(Product.region_id == Region.id))
                                    .where(expression)
                                    .distinct().dicts()
                                )
                        ]
        except Exception as e:
            print(e)
            abort(400,message="Something went wrong")  
        else:
            return { 'regions' : regions }    

class RegionDetail(Resource):

    @marshal_with(region_fields)
    def get(self,id):
        try:
            region = Region.get(Region.id == id)
        except Exception as e:
            print(e)
            abort(404, message="Not found")
        else:
            return region

# Create a Blueprint for the Resources
regions_api = Blueprint('resources.regions',__name__)        
# Create an Api from the Blueprint
api = Api(regions_api)

# Add resources
api.add_resource(
    RegionList, '/api/v1/regions',
    endpoint='regions'
)

api.add_resource(
    RegionDetail, '/api/v1/regions/detail/<int:id>',
    endpoint='region'
)