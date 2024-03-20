# routers/caja_router.py
from fastapi import APIRouter, Depends
from models.caja import Caja
from controllers.caja_controller import (
    create_caja,
    update_caja,
    get_all_cajas,
    get_caja_by_id,
    delete_caja
)
from functions.dependencies import get_current_user
from typing import List
from functions.response_descriptions import response_descriptions

router = APIRouter()

@router.post("/caja", tags=["Cajas"],  responses=response_descriptions)
def create_new_caja(caja_data: Caja, user: str = Depends(get_current_user)):
    return create_caja(caja_data, user) 

@router.put("/caja/{caja_id}", tags=["Cajas"],  responses=response_descriptions)
def update_existing_caja(caja_id: int, caja_data: Caja, user: str = Depends(get_current_user)):
    return update_caja(caja_id, caja_data, user)

@router.get("/cajas", tags=["Cajas"], response_model=List[Caja],  responses=response_descriptions)
def get_all_cajas_endpoint(  user: str = Depends(get_current_user)):
    return get_all_cajas()

@router.get("/caja/{caja_id}", tags=["Cajas"], response_model=Caja,  responses=response_descriptions)
def get_caja_by_id_endpoint(caja_id: int, user: str = Depends(get_current_user)):
    return get_caja_by_id(caja_id)

@router.delete("/caja/{caja_id}", tags=["Cajas"],  responses=response_descriptions)
def delete_caja_endpoint(caja_id: int, user: dict = Depends(get_current_user)):
    return delete_caja(caja_id,user) 