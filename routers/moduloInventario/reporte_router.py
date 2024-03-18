from fastapi import APIRouter
from controllers import reporte_controller

router = APIRouter()

@router.post("/reportes", tags=["Reporte"])
def create_reporte():
    return reporte_controller.create_reporte()

@router.get("/reportes", tags=["Reporte"])
def get_reportes():
    return reporte_controller.get_reportes()

@router.get("/reportes/{reporte_id}", tags=["Reporte"])
def get_reporte(reporte_id: int):
    return reporte_controller.get_reporte(reporte_id)

@router.delete("/reportes/{reporte_id}", tags=["Reporte"])
def delete_reporte(reporte_id: int):
    return reporte_controller.delete_reporte(reporte_id)
