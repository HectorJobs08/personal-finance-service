from bson import ObjectId
from config.database_methods import get_all
from config.database_methods import find_one
from config.database_methods import insert_one
from config.database_methods import update_one
from config.database_methods import delete_one

from models.Income import Income

table_name = "incomes"

def get_incomes()-> list[Income]:
    return get_all(table_name)

def get_income(id: str)-> Income:
    return find_one(table_name, {"_id": ObjectId(id)})

def add_income(income: Income)-> Income:
    new_income = insert_one(table_name, income.model_dump())
    return find_one(table_name, {"_id": new_income.inserted_id})

def update_income(income: Income)-> Income:
    update_fields = {
        "concept": income.concept,
        "amount": income.amount,
        "date": income.date,
        "description": income.description
    }
    update_one(table_name, {"_id": ObjectId(income.id)}, update_fields)
    return find_one(table_name, {"_id": ObjectId(income.id)})

def delete_income(id: str)-> bool:
    try:
        delete_one(table_name, {"_id": ObjectId(id)})
        return True
    except Exception as e:
        print(e)
        return False