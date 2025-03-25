from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from models.Category import Category

class TransactionResponse(BaseModel):
    id: Optional[str] = ""
    category_id: str
    concept: str
    amount: float
    type: str
    description: str | None = None
    category: Category
    created_at: datetime = datetime.now()
