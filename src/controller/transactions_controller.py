from bson import ObjectId
from config.database_methods import get_all
from config.database_methods import find_one
from config.database_methods import insert_one
from config.database_methods import update_one
from config.database_methods import delete_one

from controller.categories_controller import get_category

from models.Transaction import Transaction
from models.responses.TransactionResponse import TransactionResponse

table_name = "transactions"

def get_transactions()-> list[TransactionResponse]:
    transactions = get_all(table_name)
    for transaction in transactions:
        transaction['category'] = get_category(transaction['category_id'])
    return transactions

def get_transaction(id: str)-> TransactionResponse:
    transaction = find_one(table_name, {"_id": ObjectId(id)})
    transaction['category'] = get_category(transaction['category_id'])
    return transaction

def add_transaction(transaction: Transaction)-> TransactionResponse:
    new_transaction = insert_one(table_name, transaction.model_dump())
    print('new_transaction', new_transaction)
    return get_transaction(str(new_transaction.inserted_id))

def update_transaction(id: str, transaction: Transaction)-> TransactionResponse:
    update_fields = {
        "category_id": transaction.category_id,
        "concept": transaction.concept,
        "amount": transaction.amount,
        "type": transaction.type,
        "description": transaction.description,
        "created_at": transaction.created_at,
    }
    update_one(table_name, {"_id": ObjectId(id)}, update_fields)
    return get_transaction(id)

def delete_transaction(id: str)-> bool:
    try:
        delete_one(table_name, {"_id": ObjectId(id)})
        return True
    except Exception as e:
        print(e)
        return False