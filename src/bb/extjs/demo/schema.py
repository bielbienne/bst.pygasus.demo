from bb.extjs.core import ext

from zope import schema
from zope.interface import Interface



@ext.scaffolding('Card', 'Magic the Gathering')
class ICard(Interface):
    id = schema.Id(title = 'ID',
                   required = True,
                   )
    
    type = schema.TextLine(title = 'Type',
                            required = True,
                            )

    text = schema.TextLine(title = 'Text',
                           required = True
                           )
    
    costs = schema.Int(title = 'Costs',
                            required = False,
                            )
    
    colors = schema.TextLine(title = 'Colors',
                                 required = True,
                                 )    
    
    layout = schema.TextLine(title = 'Layout',
                               required = True,
                               )
    
    name = schema.TextLine(title = 'Name',
                       required = True,
                       )
    
    power = schema.TextLine(title = 'Power',
                       required = False,
                       )
    
    toughness = schema.TextLine(title = 'Toughness',
                       required = False,
                       )
    