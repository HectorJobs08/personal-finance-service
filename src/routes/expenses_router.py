from fastapi import APIRouter
from models.Expense import Expense
from controller.expenses_controller import get_expenses
from controller.expenses_controller import get_expense
from controller.expenses_controller import add_expense
from controller.expenses_controller import update_expense
from controller.expenses_controller import delete_expense

expenses_router = APIRouter(prefix="/expenses", tags=["Expenses"])


@expenses_router.get("", response_model=list[Expense], status_code=200)
async def get_all_expenses()-> list[Expense]:
    return get_expenses()


@expenses_router.get("/{id}", response_model=Expense, status_code=200)
async def get_expense_by_id(id: str)-> Expense:
    return get_expense(id)


@expenses_router.post("", response_model=Expense, status_code=201)
async def create_expense(expense: Expense)-> Expense:
    return add_expense(expense)


@expenses_router.put("", response_model=Expense, status_code=200)
async def update_expense_by_id(expense: Expense)-> Expense:
    return update_expense(expense)


@expenses_router.delete("/{id}", status_code=200)
async def delete_expense_by_id(id: str)-> bool:
    return delete_expense(id)