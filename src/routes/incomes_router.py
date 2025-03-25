from fastapi import APIRouter
from models.Income import Income
from controller.incomes_controller import get_incomes
from controller.incomes_controller import get_income
from controller.incomes_controller import add_income
from controller.incomes_controller import update_income
from controller.incomes_controller import delete_income

incomes_router = APIRouter(prefix="/incomes", tags=["Incomes"])

@incomes_router.get("", response_model=list[Income], status_code=200)
async def get_all_incomes():
    return get_incomes()

@incomes_router.get("/{id}", response_model=Income, status_code=200)
async def get_income_by_id(id: str)-> Income:
    return get_income(id)

@incomes_router.post("", response_model=Income, status_code=201)
def create_income(income: Income)-> Income:
    return add_income(income)

@incomes_router.put("", response_model=Income, status_code=200)
def edit_income(income: Income)-> Income:
    return update_income(income)

@incomes_router.delete("/{id}", status_code=200)
def destroy_income(id: str)-> bool:
    return delete_income(id)