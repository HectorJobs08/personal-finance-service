from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Income(BaseModel):
    id: Optional[str] = "" 
    concept: str
    amount: float
    description: str | None = None
    date: datetime = datetime.now()