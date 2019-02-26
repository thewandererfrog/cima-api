from flask import Blueprint
from flask_restful import Resource,Api,marshal,marshal_with,fields,abort,reqparse
import json

from models import Market,Product

market_fields = {
    'id' : fields.Integer,
    'name' : fields.String
}

class MarketList(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('species_id',required=True,type=int,location='args')
        self.reqparse.add_argument('variety_id',type=int,location='args')
        self.reqparse.add_argument('category_id',type=int,location='args')
        self.reqparse.add_argument('packaging_id',type=int,location='args')
        self.reqparse.add_argument('caliber_id',type=int,location='args')
        self.reqparse.add_argument('region_id',type=int,location='args')
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
            markets = [marshal(market,market_fields) 
                            for market in (
                                Product
                                    .select(Product.market.alias('id'),Market.name)
                                    .join(Market, on=(Product.market == Market.id))
                                    .where(expression)
                                    .distinct().dicts()
                                )
                        ]
        except Exception as e:
            print(e)
            abort(400,message="Something went wrong")  
        else:
            return { 'markets' : markets }     

class MarketDetail(Resource):

    @marshal_with(market_fields)
    def get(self,id):
        try:
            market = Market.get(Market.id == id)
        except Exception as e:
            print(e)
            abort(404,message="Not found")
        else:
            return market    

# Create a Blueprint for the Resources
markets_api = Blueprint('resources.markets',__name__)        
# Create an Api from the Blueprint
api = Api(markets_api)

# Add resources
api.add_resource(
    MarketList, '/api/v1/markets',
    endpoint='markets'
)

api.add_resource(
    MarketDetail, '/api/v1/markets/detail/<int:id>',
    endpoint='market'
)