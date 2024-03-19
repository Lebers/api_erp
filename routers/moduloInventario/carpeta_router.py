# routers/carpeta_router.py
from fastapi import APIRouter, Depends
from models.carpeta import Carpeta
from models.carpeta import MultipleCarpetasCreate
from controllers.carpeta_controller import (
    create_carpeta,
    update_carpeta,
    get_all_carpetas,
    get_carpeta_by_id,
    delete_carpeta,
    create_multiple_carpetas,
    get_all_carpetas_by_caja_id
)
from functions.dependencies import get_current_user 
from typing import List

router = APIRouter()

@router.post("/carpeta", tags=["Carpetas"])
def create_new_carpeta(carpeta_data: Carpeta, user: str = Depends(get_current_user)):
    return create_carpeta(carpeta_data, user)

@router.post("/carpetas", tags=["Carpetas"])
def create_multiple_carpetas_endpoint(carpeta_data: MultipleCarpetasCreate, user: str = Depends(get_current_user)):
    return create_multiple_carpetas(carpeta_data, user)

@router.put("/carpeta/{carpeta_id}", tags=["Carpetas"])
def update_existing_carpeta(carpeta_id: int, carpeta_data: Carpeta, user: str = Depends(get_current_user)):
    return update_carpeta(carpeta_id, carpeta_data, user)

@router.get("/carpetas", tags=["Carpetas"], response_model=List[Carpeta])
def get_all_carpetas_endpoint( user: str = Depends(get_current_user)):
    return get_all_carpetas()

@router.get("/carpeta/{carpeta_id}", tags=["Carpetas"], response_model=Carpeta)
def get_carpeta_by_id_endpoint(carpeta_id: int, user: str = Depends(get_current_user)):
    return get_carpeta_by_id(carpeta_id)

@router.delete("/carpeta/{carpeta_id}", tags=["Carpetas"])
def delete_carpeta_endpoint(carpeta_id: int, user: str = Depends(get_current_user)):
    return delete_carpeta(carpeta_id,user)
 
 
@router.get("/carpetasby/caja/{carpeta_id}", tags=["Carpetas"], response_model=Carpeta)
def get_carpeta_by_id_endpoint(carpeta_id: int, user: str = Depends(get_current_user)):
    return get_all_carpetas_by_caja_id(carpeta_id)
 
