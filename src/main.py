from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routes
from routes.categories_router import categories_router
from routes.transactions_router import transactions_router


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

app.include_router(transactions_router)
app.include_router(categories_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}