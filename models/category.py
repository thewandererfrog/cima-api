from peewee import *

from database import getDB

class Category(Model):
    id = BigAutoField(unique=True)
    name = CharField()

    class Meta:
        database = getDB()
