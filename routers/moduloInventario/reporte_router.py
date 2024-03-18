from fastapi import APIRouter, Depends
from controllers import reporte_controller
from datetime import date
from typing import List
from models.caja import Caja
from models.carpeta import Carpeta

from functions.dependencies import get_current_user



router = APIRouter()

@router.get("/reportes/cajas", tags=["Reportes"], response_model=List[Caja])
def reporte_cajas(fecha_inicio: date, fecha_fin: date, user: str = Depends(get_current_user)):
    return reporte_controller.get_reporte_cajas(fecha_inicio, fecha_fin)

@router.get("/reportes/carpetas", tags=["Reportes"], response_model=List[Carpeta])
def reporte_carpetas(fecha_inicio: date, fecha_fin: date, user: str = Depends(get_current_user)):
    return reporte_controller.get_reporte_carpetas(fecha_inicio, fecha_fin)
