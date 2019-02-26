from peewee import *

from models import (
    Group,
    Species,
    Variety,
    Category,
    Caliber,
    Packaging,
    Market,
    Region
)
from database import getDB

class Product(Model):
    id = BigAutoField(unique=True)
    group = ForeignKeyField(Group.id)
    species = ForeignKeyField(Species.id)
    variety = ForeignKeyField(Variety.id)
    category = ForeignKeyField(Category.id)
    caliber = ForeignKeyField(Caliber.id)
    packaging = ForeignKeyField(Packaging.id)
    market = ForeignKeyField(Market.id)
    region = ForeignKeyField(Region.id)
    price_unit = CharField(max_length=50)
    date = DateTimeField()
    min = FloatField()
    max = FloatField()
    mean = FloatField()

    class Meta:
        database = getDB()
