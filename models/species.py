from peewee import *

from database import Database
from .group import Group

class Species(Model):
    id = BigAutoField(unique=True)
    name = CharField()
    group_id = ForeignKeyField(Group.id)

    class Meta:
        database = Database.getInstance()
