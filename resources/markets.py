from flask import Blueprint
from flask_restful import Resource,Api
import json

from models import Market

class MarketList(Resource):
    def get(self):
        try:
            markets = Market.select().dicts()
            print(list(markets))    
            return json.dumps(list(markets))
        except:
            return "No records found"    

class MarketDetail(Resource):
    def get(self,id):
        try:
            market = Market.select().where(Market.id == id).dicts(True).get()
            return json.dumps(market)
        except:
            return "No records found"    

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