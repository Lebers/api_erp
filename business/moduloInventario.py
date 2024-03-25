# business/business_logic.py
from dataAccess.moduloInventario import ModuloInventario_DataAccess as MI_DataAccess
import jwt
import os
from datetime import datetime, timedelta
import bcrypt

from models.user import User as userModel

_dataAccess = MI_DataAccess()

class UserBusiness:
    def __init__(self):
        self.user_data_access = MI_DataAccess()

    def verify_password(self, db_password, password):
        # Convertir la contraseña ingresada a bytes, si aún no lo está
        password_bytes = password.encode('utf-8')
        
        # Convertir el hash de la base de datos a bytes, si aún no lo está
        db_password_bytes = db_password.encode('utf-8') if isinstance(db_password, str) else db_password
        
        # Verificar la contraseña ingresada contra el hash almacenado
        return bcrypt.checkpw(password_bytes, db_password_bytes)

    def generate_token(self, user_record):
        payload = {
            'user_id': user_record['id'],
            'username': user_record['username'],  # Incluyendo el nombre de usuario en el token
            'exp': datetime.utcnow() + timedelta(days=1)  # El token expira en 1 día
        }
        token = jwt.encode(payload, os.getenv('SECRET_KEY'), algorithm='HS256')
        return token

    def authenticate_user(self, username: str, password: str):
        response = self.user_data_access.get_user_by_username(username)
        data, log_id, *rest = response

        if data:
            if self.verify_password(data["password"], password):
                return self.generate_token(data), None, 200,"Acceso corecto"
            return None, None, 200 ,"Contraseña incorrecta"
        else:
            return None, None, 200 ,"Usuario no existe"
 
 
        
    
    def create_user(self, user: userModel):
        if _dataAccess.user_exists(user.username):
            return None, None, 409, "Usuario ya existe"

        hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
        user.password = hashed_password.decode('utf-8')
 
        response = _dataAccess.create_user(user)

        user_record, log_id, *rest = response
        status_code = rest[0] if rest else 200

        return user_record, log_id, status_code,"Usuario creado"
    

    def update_user(self, user_id: int, user: userModel):

        hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
        user.password = hashed_password.decode('utf-8')
        _dataAccess.update_user(user_id, user)
        return user_id, "Usuario actualizado", 200
    
    def get_all_users(self):
        response =_dataAccess.get_all_users()

        data, log_id, *rest = response
        status_code = rest[0] if rest else 200

        return data, log_id, status_code,"Datos de usuario"

    def get_user_by_id(self, user_id: int):
        response =_dataAccess.get_user_by_id(user_id)

        data, log_id, *rest = response
        status_code = rest[0] if rest else 200

        return data, log_id, status_code,"Datos de usuario" 
    
    def delete_user(self, user_id: int):
        response = self.user_data_access.delete_user(user_id)
        log_id, status_code, msg = response

        return log_id, status_code, msg