import pymongo

uri = 'mongodb+srv://hs503:hs503@hs503.eq243wd.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient(uri)
db = client["master"]
col = db["aeye"]


def insertData(data):
    x = col.insert_one(data)
    print(x.inserted_id)
# print the ID of the inserted document
