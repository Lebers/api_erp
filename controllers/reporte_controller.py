# En controllers/reporte_controller.py

from typing import List
from models.caja import Caja
from models.carpeta import Carpeta
from business.CajaBusiness import CajaBusiness
from business.CarpetaBusiness import CarpetaBusiness
from datetime import date


def get_reporte_cajas(fecha_inicio: date, fecha_fin: date) -> List[Caja]:
    caja_business = CajaBusiness()
    return caja_business.get_cajas_by_fecha(fecha_inicio, fecha_fin)

def get_reporte_carpetas(fecha_inicio: date, fecha_fin: date) -> List[Carpeta]:
    carpeta_business = CarpetaBusiness()
    return carpeta_business.get_carpetas_by_fecha(fecha_inicio, fecha_fin)
