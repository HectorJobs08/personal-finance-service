from fastapi import APIRouter
from models.Incoming import Incoming
from controller.incomings_controller import get_incomings
from controller.incomings_controller import get_incoming
from controller.incomings_controller import add_incoming
from controller.incomings_controller import update_incoming
from controller.incomings_controller import delete_incoming

incomings_router = APIRouter(prefix="/incomings", tags=["Incomings"])

@incomings_router.get("", response_model=list[Incoming], status_code=200)
async def get_all_incomings():
    return get_incomings()

@incomings_router.get("/{id}", response_model=Incoming, status_code=200)
async def get_incoming_by_id(id: str)-> Incoming:
    return get_incoming(id)

@incomings_router.post("", response_model=Incoming, status_code=201)
def create_incoming(incoming: Incoming)-> Incoming:
    return add_incoming(incoming)

@incomings_router.put("", response_model=Incoming, status_code=200)
def edit_incoming(incoming: Incoming)-> Incoming:
    return update_incoming(incoming)

@incomings_router.delete("/{id}", status_code=200)
def destroy_incoming(id: str)-> bool:
    return delete_incoming(id)