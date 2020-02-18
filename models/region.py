from peewee import *

from database import Database

class Region(Model):
    id = BigAutoField(unique=True)
    name = CharField()

    class Meta:
        database = Database.getInstance("region")
