from peewee import *

from database import getDB

class Region(Model):
    id = BigAutoField(unique=True)
    name = CharField()

    class Meta:
        database = getDB()
