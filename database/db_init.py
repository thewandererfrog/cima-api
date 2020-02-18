import time
import os

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
from .db_connect import Database

def initialize():
    print("Running init!")
    DATABASE = Database.getInstance("init")
    DATABASE.connect()
    print(DATABASE)
    try:
        DATABASE.connect()
    except Exception as e:
        print("Exception")
        print(e)
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