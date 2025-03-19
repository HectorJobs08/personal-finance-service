from bson import ObjectId
from config.database_methods import get_all
from config.database_methods import find_one
from config.database_methods import insert_one
from config.database_methods import update_one
from config.database_methods import delete_one

from models.Expense import Expense

table_name = "expenses"

def get_expenses()-> list[Expense]:
    return get_all(table_name)

def get_expense(id: str)-> Expense:
    return find_one(table_name, {"_id": ObjectId(id)})

def add_expense(expense: Expense)-> Expense:
    new_expense = insert_one(table_name, expense.model_dump())
    return find_one(table_name, {"_id": new_expense.inserted_id})

def update_expense(expense: Expense)-> Expense:
    update_fields = {
        "concept": expense.concept,
        "amount": expense.amount,
        "date": expense.date,
        "description": expense.description
    }
    update_one(table_name, {"_id": ObjectId(expense.id)}, update_fields)
    return find_one(table_name, {"_id": ObjectId(expense.id)})

def delete_expense(id: str)-> bool:
    try:
        delete_one(table_name, {"_id": ObjectId(id)})
        return True
    except Exception as e:
        print(e)
        return False