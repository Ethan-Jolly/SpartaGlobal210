import pymongo
print(pymongo.version)

client = pymongo.MongoClient('mongodb://3.124.188.231:27017')

db = client['demo']
col = db['test_collection']

col.insert_one({'success': True})

for document in col.find():
    print(document)
