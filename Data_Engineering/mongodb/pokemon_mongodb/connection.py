import os
from pymongo import MongoClient
from dotenv import load_dotenv
import requests
import random

class Client:
    def __init__(self, MONGODB_URI, db_name, collection_name):
        self.MONGODB_URI = MONGODB_URI
        self.db_name = db_name
        self.collection_name = collection_name
        self.client = MongoClient(self.MONGODB_URI, serverSelectionTimeoutMS=5000)
        self.db = self.client[self.db_name]
        self.coll = self.db[self.collection_name]

    def load_documents_in_cluster(self, documents):
        for doc in documents['results']:
            response = requests.get(doc["url"])
            self.coll.update_one({"name":response.json()['name']},{"$setOnInsert":response.json()},upsert=True)

    def get_collection(self):
        return self.coll
    
    def update_document_by_name(self, name, field_name, value):
        self.coll.update_one({"name":name}, {"$inc": {field_name: value}})

    def get_top_n(self, field_name, limit):
        top = self.coll.aggregate([
            {'$sort': {field_name: -1, 'name':1 }},
            {'$project': {field_name: 1, 'name': 1}}, 
            {'$match': {field_name: {
                        '$gt': 0
                    }
                }
            }, 
            {'$limit': limit}
        ])
        return list(top)

# Loads all data from api in to cluster
def main():
    load_dotenv()
    MONGODB_URI = os.environ["MONGODB_URI"]
    client = Client(MONGODB_URI, 'pokemon_data', 'pokemon')
    
    pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=1118').json()
    client.load_documents_in_cluster(pokemon)

if __name__ == '__main__':
    main()

