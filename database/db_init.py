from models import Group,Species
from .db_connect import getDB

def initialize():
    DATABASE = getDB()
    DATABASE.connect()
    DATABASE.create_tables([Group,Species], safe=True)
    DATABASE.close()