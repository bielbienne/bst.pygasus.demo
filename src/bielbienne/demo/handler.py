from bb.extjs.core import ext

from bb.extjs.wsgi.interfaces import IRequest

from bielbienne.demo import model

from whoosh.index import create_in, open_dir, EmptyIndexError
from whoosh.fields import TEXT, NUMERIC, STORED, Schema
from whoosh.qparser import QueryParser

import copy
import json
import os

data = dict()
cards = list()
ix = None


class CardHandler(ext.AbstractModelHandler):
    ext.adapts(model.Card, IRequest)
    
    def get(self, model, batch):
        global ix
        
        try:
            ix = open_dir("index")
        except EmptyIndexError:
            schema = Schema(id=NUMERIC(unique=True), name=TEXT, type=TEXT,
                            layout=TEXT, text=TEXT, colors=TEXT,
                            costs=NUMERIC, power=TEXT, toughness=TEXT,
                            card=STORED)

            if not os.path.exists("index"):
                os.mkdir("index")            
            
            ix = create_in("index", schema)
            writer = ix.writer()
             
            file_path = os.path.join(os.path.dirname(__file__), 'app/resources/AllCards.json')
            self.read_json(file_path)
            id = 1
            for key in data.keys():
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
                                    card=copy.deepcopy(model))
                
            writer.commit()
            data.clear()
                
                  
   
        start, limit = self.slice()
        
        property, direction = self.sort()
        
        with ix.searcher() as searcher:
            cards.clear()
            query = QueryParser('', ix.schema).parse('*')
            page = int(start / limit) + 1
            if direction == 'ASC':
                direction=False
            else:
                direction=True
            results = searcher.search_page(query, page, pagelen=limit, sortedby=property, reverse=direction)
            for result in results:
                cards.append(result['card'])
        
        return cards, len(cards)

    def create(self, model, batch):
        return [model]
    
    def update(self, model, batch):
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
                                       card=copy.deepcopy(model))
                
                writer.commit()
                
        return [model], 1
    
    def read_json(self, path):
        global data
        if len(data) == 0:
            with open(path) as data_file:
                data = json.load(data_file)
