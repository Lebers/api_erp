# controllers/carpeta_controller.py

# Importamos las librerías necesarias
from fastapi import HTTPException
from models.carpeta import Carpeta as CarpetaModel
from business.CarpetaBusiness import CarpetaBusiness
from functions.api_response import ApiResponse
from models.carpeta import MultipleCarpetasCreate
from typing import List
from datetime import datetime



# Creamos una instancia de la clase CarpetaBusiness
carpeta_business = CarpetaBusiness()

def handle_response(response, success_data):
    data, log_id, status_code, msg = response
    if data:
        return ApiResponse.success(success_data, msg)
    else:
        return ApiResponse.error(msg, log_id, status_code)

def create_carpeta(carpeta_data: CarpetaModel, current_user: dict):
    carpeta_data.createUser = current_user.get('username')
    response = carpeta_business.create_carpeta(carpeta_data)
    return handle_response(response, {"carpeta_id": response[0]})

def update_carpeta(carpeta_id: int, carpeta_data: CarpetaModel, current_user: dict):
    carpeta_data.updateUser = current_user.get('username')
    response = carpeta_business.update_carpeta(carpeta_id, carpeta_data)
    return handle_response(response, {"carpeta_id": response[0]})

def get_all_carpetas():
    response = carpeta_business.get_all_carpetas()
    carpetas_list = [carpeta.dict() for carpeta in response[0]]
    return handle_response(response, {"carpetas": carpetas_list})

def get_carpeta_by_id(carpeta_id: int):
    response = carpeta_business.get_carpeta_by_id(carpeta_id)
    return handle_response(response, {"carpeta": response[0].dict()})

# Esta función elimina una carpeta por su id
def delete_carpeta(carpeta_id: int,current_user: dict):
    user = current_user.get('username')
    try:
        response = carpeta_business.delete_carpeta(carpeta_id,user)
        log_id, status_code, msg = response

        if status_code == 200:
            return ApiResponse.success({"carpeta_id": carpeta_id}, msg)
        else:
            return ApiResponse.error(msg, log_id, status_code)
    except Exception as e:
        print("Exception", e)
        return ApiResponse.error(str(e), 0, 409) 

def create_multiple_carpetas(carpeta_data: MultipleCarpetasCreate, user: dict):
    response = carpeta_business.create_multiple_carpetas(carpeta_data, user)
    return handle_response(response, []) 

def get_all_carpetas_by_caja_id(caja_id: int):
    total_carpetas = carpeta_business.get_total_carpetas_by_caja_id(caja_id)
    response = carpeta_business.get_all_carpetas_by_caja_id(caja_id)

    print("total_carpetas-total_carpetas", total_carpetas)
    print("response-response", response)
    
    # Verificar si hay carpetas en la respuesta
    if response:
        # Si hay carpetas, no necesitas convertirlas en formato de diccionario
        carpetas_list = response[0]  # No es necesario usar comprensión de lista aquí
        return handle_response(response, {"carpetas": carpetas_list, "amount": total_carpetas[0]})
    else:
        # Si no hay carpetas, devolver un mensaje de error apropiado
        return handle_response(response, {"message": "No hay carpetas asociadas a esta caja"})
 
