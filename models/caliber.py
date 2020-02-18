from peewee import *

from database import Database

class Caliber(Model):
    id = BigAutoField(unique=True)
    name = CharField()

    class Meta:
        database = Database.getInstance("caliber")
