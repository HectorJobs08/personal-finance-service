from fastapi import APIRouter
from models.Category import Category
from controller.categories_controller import get_categories
from controller.categories_controller import get_category
from controller.categories_controller import add_category
from controller.categories_controller import update_category
from controller.categories_controller import delete_category

categories_router = APIRouter(prefix="/categories", tags=["Categories"])

@categories_router.get("", response_model=list[Category], status_code=200)
async def get_all_categories()-> list[Category]:
    return get_categories()

@categories_router.get("/{id}", response_model=Category, status_code=200)
async def get_category_by_id(id: str)-> Category:
    return get_category(id)

@categories_router.post("", response_model=Category, status_code=201)
async def create_category(category: Category)-> Category:
    return add_category(category)

@categories_router.put("", response_model=Category, status_code=200)
async def update_category_by_id(category: Category)-> Category:
    return update_category(category)

@categories_router.delete("/{id}", status_code=200)
async def delete_category_by_id(id: str)-> bool:
    return delete_category(id)