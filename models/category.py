from peewee import *

from database import Database

class Category(Model):
    id = BigAutoField(unique=True)
    name = CharField()

    class Meta:
        database = Database.getInstance("category")
