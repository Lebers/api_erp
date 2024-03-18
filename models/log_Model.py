# models/log.py
from pydantic import BaseModel
from datetime import datetime

class Log(BaseModel):
    id: int
    message: str
    created_at: datetime

 