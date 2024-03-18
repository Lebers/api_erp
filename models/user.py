 # models/user.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class User(BaseModel):
    name: str
    username: str
    password: str
    
class UserInDB(BaseModel):
    id: int
    username: str
    name: str
    createDate: datetime
    updateDate: Optional[datetime] = None

    def dict(self, **kwargs):
        d = super().dict(**kwargs)
        d['createDate'] = self.createDate.isoformat() if self.createDate else None
        d['updateDate'] = self.updateDate.isoformat() if self.updateDate else None
        return d