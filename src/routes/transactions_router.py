from fastapi import APIRouter
from models.Transaction import Transaction
from models.responses.TransactionResponse import TransactionResponse
from controller.transactions_controller import get_transactions
from controller.transactions_controller import get_transaction
from controller.transactions_controller import add_transaction
from controller.transactions_controller import update_transaction
from controller.transactions_controller import delete_transaction

transactions_router = APIRouter(prefix="/transactions", tags=["Transactions"])

@transactions_router.get("", response_model=list[TransactionResponse], status_code=200)
async def get_all_transactions()-> list[TransactionResponse]:
    return get_transactions()

@transactions_router.get("/{id}", response_model=TransactionResponse, status_code=200)
async def get_transaction_by_id(id: str)-> TransactionResponse:
    return get_transaction(id)

@transactions_router.post("", response_model=TransactionResponse, status_code=201)
def create_transaction(transaction: Transaction)-> TransactionResponse:
    return add_transaction(transaction)

@transactions_router.put("/{id}", response_model=TransactionResponse, status_code=200)
def edit_transaction(id: str, transaction: Transaction)-> TransactionResponse:
    return update_transaction(id, transaction)

@transactions_router.delete("/{id}", status_code=200)
def destroy_transaction(id: str)-> bool:
    return delete_transaction(id)