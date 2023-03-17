import os
from pymongo import MongoClient
from dotenv import load_dotenv
import requests

load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]
# set a 5-second connection timeout
client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)

db = client['star_wars']
people_col = db['people']
starship_col = db['starships']


def save_people_docs(col):
    response = requests.get("https://swapi.dev/api/people/").json()['results']
    for doc in response:
        col.update_one({"name":doc['name']},{"$setOnInsert":doc},upsert=True)

def save_starship_docs(col):
    response = requests.get("https://swapi.dev/api/starships/").json()['results']
    for doc in response:
        col.update_one({"model":doc['model']},{"$setOnInsert":doc},upsert=True)

save_people_docs(people_col)
save_starship_docs(starship_col)