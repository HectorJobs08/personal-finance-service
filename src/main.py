from fastapi import FastAPI

# Routes
from routes.incomings_router import incomings_router
from routes.expenses_router import expenses_router

app = FastAPI()

app.include_router(incomings_router)
app.include_router(expenses_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}