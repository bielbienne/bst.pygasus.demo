from bb.extjs.core import ext
from bb.extjs.demo import schema

class Card(ext.Model):
    ext.schema(schema.ICard)
    id = 0 
    type = ''
    text = ''
    costs = 0
    colors = ''
    layout = ''
    name = ''
    power = ''
    toughness = ''
    