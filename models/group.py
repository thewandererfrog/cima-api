from peewee import *

from database import Database
a= "group"
class Group(Model):
    id = BigAutoField(unique=True)
    name = CharField()

    class Meta:
        database = Database.getInstance(a)
