# controllers/caja_controller.py

# Importamos las librerías necesarias
from fastapi import HTTPException
from models.caja import Caja as CajaModel
from business.CajaBusiness import CajaBusiness
from functions.api_response import ApiResponse
from datetime import datetime


# Creamos una instancia de la clase CajaBusiness
caja_business = CajaBusiness()

# Esta función maneja la respuesta de las operaciones CRUD
# Si la operación es exitosa, retorna un mensaje de éxito, en caso contrario, retorna un mensaje de error
def handle_response(response, success_data):
    data, log_id, status_code, msg = response
    if data:
        return ApiResponse.success(success_data, msg)
    else:
        return ApiResponse.error(msg, log_id, status_code)

# Esta función crea una nueva caja, toma como parámetros los datos de la caja y el usuario actual
def create_caja(caja_data: CajaModel, current_user: dict):
    print("caja_data-caja_data:",caja_data)
    caja_data.createUser = current_user.get('username')
    response = caja_business.create_caja(caja_data)
    return handle_response(response, {"caja_id": response[0]})

# Esta función actualiza una caja existente, toma como parámetros el id de la caja y los nuevos datos de la caja
def update_caja(caja_id: int, caja_data: CajaModel, current_user: dict):
    caja_data.updateUser = current_user.get('username')
    response = caja_business.update_caja(caja_id, caja_data)
    return handle_response(response, {"caja_id": response[0]})

# Esta función obtiene una caja por su id
def get_caja_by_id(caja_id: int):
    response = caja_business.get_caja_by_id(caja_id)
    return handle_response(response, {"caja": response[0].dict()})

# Esta función obtiene todas las cajas
def get_all_cajas():
    response = caja_business.get_all_cajas()
    cajas_list = []

    for caja in response[0]:
        caja_dict = caja.dict()
        # Convertir los objetos datetime a cadenas de texto en formato ISO 8601
        caja_dict['createDate'] = caja_dict['createDate'].isoformat() if caja_dict['createDate'] else None
        caja_dict['updateDate'] = caja_dict['updateDate'].isoformat() if caja_dict['updateDate'] else None
        caja_dict['deleteDate'] = caja_dict['deleteDate'].isoformat() if caja_dict['deleteDate'] else None
        cajas_list.append(caja_dict)

    return handle_response(response, {"cajas": cajas_list})

# Esta función elimina una caja por su id
def delete_caja(caja_id: int,current_user: dict):
    user = current_user.get('username')
    try:
        response = caja_business.delete_caja(caja_id,user)
        log_id, status_code, msg = response

        if status_code == 200:
            return ApiResponse.success({"caja_id": caja_id}, msg)
        else:
            return ApiResponse.error(msg, log_id, status_code)
    except Exception as e:
        print("Exception", e)
        return ApiResponse.error(str(e), 0, 409) 