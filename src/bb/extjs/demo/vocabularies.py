from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


def card_availability(context):
    return SimpleVocabulary([
                             SimpleTerm('1', '1', '1 Card'),
                             SimpleTerm('2', '2', '2 Cards'),
                             SimpleTerm('3', '3', '3 Cards'),
                             SimpleTerm('4', '4', '4 Cards'),
                             SimpleTerm('5', '5', '5 Cards')
                             ])