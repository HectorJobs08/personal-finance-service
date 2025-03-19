from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Incoming(BaseModel):
    id: Optional[str] = "" 
    concept: str
    amount: float
    description: str | None = None
    date: datetime = datetime.now()