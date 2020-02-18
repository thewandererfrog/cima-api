from peewee import *

from models import (
    Species,
    Variety,
    Category,
    Caliber,
    Packaging,
    Market,
    Region
)
from database import Database

class Product(Model):
    id = BigAutoField(unique=True)
    species_id = ForeignKeyField(Species.id)
    variety_id = ForeignKeyField(Variety.id)
    category_id = ForeignKeyField(Category.id)
    caliber_id = ForeignKeyField(Caliber.id)
    packaging_id = ForeignKeyField(Packaging.id)
    market_id = ForeignKeyField(Market.id)
    region_id = ForeignKeyField(Region.id)
    price_unit_id = CharField(max_length=50)
    date = DateTimeField()
    min = FloatField()
    max = FloatField()
    mean = FloatField()

    class Meta:
        database = Database.getInstance()
