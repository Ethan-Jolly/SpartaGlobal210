import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]
# set a 5-second connection timeout
client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)

db = client['sample_airbnb']
coll = db['listingsAndReviews']

# Finding a document
print(coll.find_one({"bedrooms": 7},{"name": 1,"property_type": 1,"room_type": 1,
    "bedrooms": 1,"beds": 1,"price": 1,"number_of_reviews": 1}))

print('---------------------------------------------------------')

# Inserting in a new document
inserted_id = coll.insert_one({"name":"big house","beds":0,"bedrooms":0,"number_of_reviews":1000,"price":6}).inserted_id
print(coll.find_one({"_id":inserted_id}))

print('---------------------------------------------------------')

# Finding a document using a filter with an operator
print(coll.find_one({"bedrooms": {"$gte":8}},{"name": 1,"property_type": 1,"room_type": 1,
    "bedrooms": 1,"beds": 1,"price": 1,"number_of_reviews": 1}))

print('---------------------------------------------------------')

# Finding many documents and sorting by price
doc = coll.find({"bedrooms": {"$gte":9}},{"name": 1,"property_type": 1,"room_type": 1,
    "bedrooms": 1,"beds": 1,"price": 1,"number_of_reviews": 1}).sort("price",-1)
for x in doc:
    print(x)

print('---------------------------------------------------------')

# Deleting One document which matches the filter
print(coll.delete_one({"name":"big house"}))

print('---------------------------------------------------------')

# Updating One document which matches the filter
coll.update_one({"bedrooms":8},{"$inc":{"price":10}})
print(coll.find_one({"bedrooms":8},{"name": 1,"property_type": 1,"room_type": 1,
    "bedrooms": 1,"beds": 1,"price": 1,"number_of_reviews": 1}))

print('---------------------------------------------------------')

# Finding document and updating (Returns updated document)
print(coll.find_one_and_update({"property_type":"Apartment"},{"$inc":{"price":10}},projection={"name": 1,"property_type": 1,"room_type": 1,
    "bedrooms": 1,"beds": 1,"price": 1,"number_of_reviews": 1}))

print('---------------------------------------------------------')

# Finding one document matching filter, then replacing it with new document (Returning new document) 
print(coll.find_one_and_replace({"price":113},{"name":'find_one_replace',"price":113,"beds":2,"bedrooms":2}))

