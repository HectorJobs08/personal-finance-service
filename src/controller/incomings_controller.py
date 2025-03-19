from bson import ObjectId
from config.database_methods import get_all
from config.database_methods import find_one
from config.database_methods import insert_one
from config.database_methods import update_one
from config.database_methods import delete_one

from models.Incoming import Incoming

table_name = "incomings"

def get_incomings()-> list[Incoming]:
    return get_all(table_name)

def get_incoming(id: str)-> Incoming:
    return find_one(table_name, {"_id": ObjectId(id)})

def add_incoming(incoming: Incoming)-> Incoming:
    new_incoming = insert_one(table_name, incoming.model_dump())
    return find_one(table_name, {"_id": new_incoming.inserted_id})

def update_incoming(incoming: Incoming)-> Incoming:
    update_fields = {
        "concept": incoming.concept,
        "amount": incoming.amount,
        "date": incoming.date,
        "description": incoming.description
    }
    update_one(table_name, {"_id": ObjectId(incoming.id)}, update_fields)
    return find_one(table_name, {"_id": ObjectId(incoming.id)})

def delete_incoming(id: str)-> bool:
    try:
        delete_one(table_name, {"_id": ObjectId(id)})
        return True
    except Exception as e:
        print(e)
        return False