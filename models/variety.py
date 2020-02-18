from peewee import *

from database import Database

class Variety(Model):
    id = BigAutoField(unique=True)
    name = CharField()

    class Meta:
        database = Database.getInstance("variety")
