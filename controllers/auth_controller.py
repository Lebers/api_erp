# controllers/auth_controller.py
from business.moduloInventario import UserBusiness
from functions.api_response import ApiResponse
import jwt
import os
from datetime import datetime, timedelta



def login(username: str, password: str):
    user_business = UserBusiness()
    response = user_business.authenticate_user(username, password)
    data, log_id, status_code,msg = response
    if data:
        return ApiResponse.success({"token": data,"user":username}, msg,"status":"success",)
    else:
        return ApiResponse.error(msg, log_id,status_code)
 
def crear_token(user_id: int):
    # Lógica para crear un nuevo token
    return {"token": "new_token"}

def verificar_token(token: str):
    # Lógica para verificar la validez del token
    return {"token_valid": True}

def generate_token(user_info):
    payload = {
        'user_id': user_info['user_id'],
        'username': user_info['username'],
        'exp': datetime.utcnow() + timedelta(days=1)  # Ajusta según tus necesidades
    }
    return jwt.encode(payload, os.getenv('SECRET_KEY'), algorithm='HS256')


def refresh_token(current_user):
    # Asumiendo que current_user contiene la información necesaria para generar un nuevo token
    if current_user:
        new_token = generate_token(current_user)
        return {"token": new_token}
    else:
        # Manejar caso en que current_user no es válido
        return {"error": "Invalid token or user"}
