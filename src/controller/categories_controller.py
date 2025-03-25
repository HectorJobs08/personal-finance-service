from bson import ObjectId
from config.database_methods import get_all
from config.database_methods import find_one
from config.database_methods import insert_one
from config.database_methods import update_one
from config.database_methods import delete_one

from models.Category import Category

table_name = "categories"

def get_categories()-> list[Category]:
    return get_all(table_name)

def get_category(id: str)-> Category:
    return find_one(table_name, {"_id": ObjectId(id)})

def add_category(category: Category)-> Category:
    new_category = insert_one(table_name, category.model_dump())
    return find_one(table_name, {"_id": new_category.inserted_id})

def update_category(category: Category)-> Category:
    update_fields = {
        "name": category.name,
        "icon": category.icon
    }

    update_one(table_name, {"_id": ObjectId(category.id)}, update_fields)
    return find_one(table_name, {"_id": ObjectId(category.id)})

def delete_category(id: str)-> bool:
    try:
        delete_one(table_name, {"_id": ObjectId(id)})
        return True
    except Exception as e:
        print(e)
        return False
