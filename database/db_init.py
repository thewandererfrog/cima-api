from models import (
    Group,
    Species,
    Variety,
    Category,
    Caliber,
    Market,
    Region,
    Packaging,
    Product
)
from .db_connect import getDB

def initialize():
    DATABASE = getDB()
    DATABASE.connect()
    DATABASE.create_tables([
        Group,
        Species,
        Variety,
        Category,
        Caliber,
        Packaging,
        Market,
        Region,
        Product
        ], safe=True)
    DATABASE.close()