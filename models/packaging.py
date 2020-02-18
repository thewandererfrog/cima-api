from peewee import *

from database import Database

class Packaging(Model):
    id = BigAutoField(unique=True)
    name = CharField()

    class Meta:
        database = Database.getInstance("packaging")
