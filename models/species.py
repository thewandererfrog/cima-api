from peewee import *

from database import getDB
from .group import Group

class Species(Model):
    id = BigAutoField(unique=True)
    name = CharField()
    group_id = ForeignKeyField(Group.id)
    external_id = IntegerField()

    class Meta:
        database = getDB()
