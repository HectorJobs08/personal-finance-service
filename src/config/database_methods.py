from .connection import db
from .document_parser import parse_documents, parse_document

def get_collection(collection_name):
    return db.get_collection(collection_name)

def get_all(collection_name):
    return parse_documents(list(get_collection(collection_name).find({})))

def find_one(collection_name, query):
    return parse_document(get_collection(collection_name).find_one(query))

def insert_one(collection_name, document):
    return get_collection(collection_name).insert_one(document)

def insert_many(collection_name, documents):
    return get_collection(collection_name).insert_many(documents)

def update_one(collection_name, query, update):
    return get_collection(collection_name).update_one(query, { "$set": update })

def update_many(collection_name, query, update):
    return get_collection(collection_name).update_many(query, update)

def delete_one(collection_name, query):
    return get_collection(collection_name).delete_one(query)

def delete_many(collection_name, query):
    return get_collection(collection_name).delete_many(query)