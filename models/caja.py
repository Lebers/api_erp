# models/caja.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from decimal import Decimal 

class Caja(BaseModel):
    id: int
    code: str  
    createDate: Optional[datetime] = Field(None, alias='createDate')
    createUser: Optional[str] = Field(None, alias='createUser')
    updateDate: Optional[datetime] = Field(None, alias='updateDate')
    updateUser: Optional[str] = Field(None, alias='updateUser')
    deleteDate: Optional[datetime] = Field(None, alias='deleteDate')
    deleteUser: Optional[str] = Field(None, alias='deleteUser')
    is_delete: Optional[bool] = Field(None, alias='is_delete')
    amount: Optional[int] = Field(0, alias='amount') 

class CajaInDB(BaseModel):
    id: int
    code: str
    createDate: Optional[datetime] = Field(None, alias='createDate')
    createUser: Optional[str] = Field(None, alias='createUser')
    updateDate: Optional[datetime] = Field(None, alias='updateDate')
    updateUser: Optional[str] = Field(None, alias='updateUser')
    deleteDate: Optional[datetime] = Field(None, alias='deleteDate')
    deleteUser: Optional[str] = Field(None, alias='deleteUser')
    amount: Optional[int] = Field(0, alias='amount') 

    def dict(self, **kwargs):
        kwargs.setdefault('exclude_none', False)
        return super().dict(**kwargs)
 
     