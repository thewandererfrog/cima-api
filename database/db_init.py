import time

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
    try:
        DATABASE.connect()
    except Exception as e:
        print(e)
        print("Exception")
        #initialize()
    finally:    
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
        # Close connection    
        DATABASE.close()