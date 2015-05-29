from bb.extjs.core import ext

from bb.extjs.wsgi.interfaces import IRequest
from bb.extjs.wsgi.interfaces import IApplicationSettings

from bb.extjs.wsgi.events import IApplicationStartupEvent

from bb.extjs.demo import model

from bb.extjs.demo.model import Card

from whoosh.index import create_in
from whoosh.index import open_dir
from whoosh.index import EmptyIndexError

from whoosh.fields import TEXT
from whoosh.fields import NUMERIC
from whoosh.fields import STORED
from whoosh.fields import KEYWORD
from whoosh.fields import Schema
from whoosh.fields import SchemaClass

from whoosh.qparser import QueryParser

from threading import Lock

import json
import os

ix = None


class CardHandler(ext.AbstractModelHandler):
    ext.adapts(model.Card, IRequest)

    def get(self, model, batch):
        start, limit = self.slice()
        property, direction = self.sort()

        return CardIndexer.search_index(start, limit, property, direction)

    def create(self, model, batch):
        model.id = CardIndexer.get_next_id()
        CardIndexer.extend_index(model)

        return [model], 1

    def update(self, model, batch):
        CardIndexer.update_index(model)

        return [model], 1


@ext.subscribe(IApplicationSettings, IApplicationStartupEvent)
def initalize_card_index(settings, event):
    CardIndexer.create_index()


class CardIndexSchema(SchemaClass):
    id = NUMERIC(unique=True, sortable=True)
    name = KEYWORD(sortable=True)
    type = KEYWORD(sortable=True)
    layout = TEXT(sortable=True)
    text = TEXT
    colors = KEYWORD(sortable=True, commas=True)
    costs = NUMERIC(sortable=True)
    power = TEXT(sortable=True)
    toughness = TEXT(sortable=True)
    card = STORED


class CardIndexer():

    def create_index():
        global ix
        data = list()

        try:
            ix = open_dir("index")
        except EmptyIndexError:
            if not os.path.exists("index"):
                os.mkdir("index")

            ix = create_in("index", CardIndexSchema())
            writer = ix.writer()

            file_path = os.path.join(os.path.dirname(__file__),
                                     'app/resources/AllCards.json')
            data = CardIndexer.read_json(file_path)
            id = 1
            for key in data.keys():
                model = Card()
                model.id = id
                id += 1
                model.type = data[key]['type']
                model.layout = data[key]['layout']
                model.name = data[key]['name']
                if 'text' in data[key].keys():
                    model.text = data[key]['text']
                if 'cmc' in data[key].keys():
                    model.costs = int(data[key]['cmc'])
                if 'power' in data[key].keys():
                    model.power = data[key]['power']
                if 'toughness' in data[key].keys():
                    model.toughness = data[key]['toughness']
                if 'colors' in data[key].keys():
                    model.colors = ', '.join(data[key]['colors'])

                writer.add_document(id=model.id,
                                    name=model.name,
                                    type=model.type,
                                    layout=model.layout,
                                    text=model.text,
                                    colors=model.colors,
                                    costs=model.costs,
                                    power=model.power,
                                    toughness=model.toughness,
                                    card=model)

            writer.commit()
            data.clear()

    def search_index(start, limit, property, direction):
        global ix
        cards = list()

        total_results = 0

        with ix.searcher() as searcher:
            cards.clear()
            query = QueryParser('', ix.schema).parse('*')
            page = int(start / limit) + 1
            if direction == 'ASC':
                direction = False
            else:
                direction = True

            results = searcher.search_page(query,
                                           page,
                                           limit,
                                           sortedby=property,
                                           reverse=direction)

            total_results = results.total

            for result in results:
                cards.append(result['card'])

        return cards, total_results

    def extend_index(model):
        writer = ix.writer()

        writer.add_document(id=model.id,
                            name=model.name,
                            type=model.type,
                            layout=model.layout,
                            text=model.text,
                            colors=model.colors,
                            costs=model.costs,
                            power=model.power,
                            toughness=model.toughness,
                            card=model)

        writer.commit()

    def update_index(model):
        global ix

        with ix.searcher() as searcher:
            query = QueryParser('id', ix.schema).parse(str(model.id))
            result = searcher.search(query)
            if len(result) == 1:
                writer = ix.writer()

                writer.update_document(id=model.id,
                                       name=model.name,
                                       type=model.type,
                                       layout=model.layout,
                                       text=model.text,
                                       colors=model.colors,
                                       costs=model.costs,
                                       power=model.power,
                                       toughness=model.toughness,
                                       card=model)

                writer.commit()

    def get_next_id():
        reader = ix.reader()
        return reader.doc_count() + 1

    def read_json(path):
        with open(path) as data_file:
            return json.load(data_file)
