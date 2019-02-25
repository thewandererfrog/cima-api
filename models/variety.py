from peewee import *

from database import getDB
from .species import Species

class Variety(Model):
    id = BigAutoField(unique=True)
    name = CharField()
    species_id = ForeignKeyField(Species.id)

    class Meta:
        database = getDB()
