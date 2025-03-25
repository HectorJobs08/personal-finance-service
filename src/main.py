from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routes
from routes.incomes_router import incomes_router
from routes.expenses_router import expenses_router

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(incomes_router)
app.include_router(expenses_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}