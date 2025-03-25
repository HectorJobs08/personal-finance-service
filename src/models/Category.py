from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Category(BaseModel):
    id: Optional[str] = "" 
    name: str
    icon: str
    created_at: datetime = datetime.now()