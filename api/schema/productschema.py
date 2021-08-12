
from api import ma

class ProductSchema(ma.Schema):
    class Meta:
        fields=("id","name","description","price","quantity")