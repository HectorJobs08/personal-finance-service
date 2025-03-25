from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Transaction(BaseModel):
    category_id: str
    concept: str
    amount: float
    type: str
    description: str | None = None
    created_at: datetime = datetime.now()
