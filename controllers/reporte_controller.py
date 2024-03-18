def create_reporte():
    # Lógica para crear un reporte
    return {"message": "Reporte created"}

def get_reportes():
    # Lógica para obtener todos los reportes
    return {"message": "Reportes fetched"}

def get_reporte(reporte_id: int):
    # Lógica para obtener un reporte específico
    return {"message": f"Reporte {reporte_id} fetched"}

def delete_reporte(reporte_id: int):
    # Lógica para eliminar un reporte
    return {"message": f"Reporte {reporte_id} deleted"}
