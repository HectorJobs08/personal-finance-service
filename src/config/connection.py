import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.get_database("finanzas")


