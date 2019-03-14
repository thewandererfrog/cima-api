from peewee import *

from database import getDB

class Group(Model):
    id = BigAutoField(unique=True)
    name = CharField()

    class Meta:
        database = getDB()
