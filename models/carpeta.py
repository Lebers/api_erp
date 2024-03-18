# models/carpeta.py
from pydantic import BaseModel, Field
from typing import Optional,List
from datetime import datetime


class Carpeta(BaseModel):
    code: str
    caja_id: int
    createDate: Optional[datetime] = Field(None, alias='createDate')
    createUser: Optional[str] = Field(None, alias='createUser')
    updateDate: Optional[datetime] = Field(None, alias='updateDate')
    updateUser: Optional[str] = Field(None, alias='updateUser')
    deleteDate: Optional[datetime] = Field(None, alias='deleteDate')
    deleteUser: Optional[str] = Field(None, alias='deleteUser')
    is_delete: Optional[bool] = Field(None, alias='is_delete')

class CarpetaInDB(BaseModel):
    id: int
    code: str
    caja_id: int
    createDate: Optional[datetime] = Field(None, alias='createDate')
    createUser: Optional[str] = Field(None, alias='createUser')
    updateDate: Optional[datetime] = Field(None, alias='updateDate')
    updateUser: Optional[str] = Field(None, alias='updateUser')
    deleteDate: Optional[datetime] = Field(None, alias='deleteDate')
    deleteUser: Optional[str] = Field(None, alias='deleteUser')
    is_delete: Optional[bool] = Field(None, alias='is_delete')

    def dict(self, **kwargs):
        d = super().dict(**kwargs)
        for key, value in d.items():
            if isinstance(value, datetime):
                d[key] = value.isoformat() if value else None
        return d
    
class MultipleCarpetasCreate(BaseModel):
    codes: List[str]
    caja_id: int
