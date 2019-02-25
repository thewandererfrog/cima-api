from peewee import *

from database import getDB
from .variety import Variety

class Category(Model):
    id = BigAutoField(unique=True)
    name = CharField()
    variety_id = ForeignKeyField(Variety.id)

    class Meta:
        database = getDB()
