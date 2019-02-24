from peewee import *

from database import getDB

class Group(Model):
    id = BigAutoField(unique=True)
    name = CharField()
    external_id = IntegerField()

    class Meta:
        database = getDB()
