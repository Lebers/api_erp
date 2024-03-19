# business/CarpetaBusiness.py
from dataAccess.CarpetaDataAccess import CarpetaDataAccess
from models.carpeta import Carpeta as CarpetaModel
from dataAccess.CajaDataAccess import CajaDataAccess
from typing import List
from models.carpeta import MultipleCarpetasCreate
from datetime import date


class CarpetaBusiness:
    def __init__(self):
        self.carpeta_data_access = CarpetaDataAccess()
        self.caja_data_access = CajaDataAccess()

    def create_carpeta(self, carpeta: CarpetaModel):
        if self.carpeta_data_access.carpeta_exists(carpeta.code):
            return None, None, 400, "Carpeta already exists"
        
        # Verificar si el caja_id asociado existe
        if not self.caja_data_access.caja_exists_by_id(carpeta.caja_id):
            return None, None, 400, "Caja ID does not exist"
        
        response = self.carpeta_data_access.create_carpeta(carpeta)
        return response
    
    

    def update_carpeta(self, carpeta_id: int, carpeta: CarpetaModel):
        if not self.carpeta_data_access.carpeta_exists_by_id(carpeta_id):
            return None, None, 400, "Carpeta ID does not exist"
        if self.carpeta_data_access.carpeta_exists(carpeta.code):
            return None, None, 400, "Carpeta code already exists"
        response = self.carpeta_data_access.update_carpeta(carpeta_id, carpeta)
        return response

    def get_carpeta_by_id(self, carpeta_id: int):
        return self.carpeta_data_access.get_carpeta_by_id(carpeta_id)

    def get_all_carpetas(self):
        return self.carpeta_data_access.get_all_carpetas()

    def carpeta_exists_by_code_and_caja_id(self, code: str, caja_id: int):
        return self.carpeta_data_access.carpeta_exists_by_code_and_caja_id(code, caja_id)
    
    def get_existing_carpetas(self, codes: List[str], caja_id: int) -> List[str]:
        existing_carpetas = []

        # Obtener todas las carpetas existentes para la caja_id dada
        existing_carpetas_data, _, _ = self.carpeta_data_access.get_existing_carpetas_data(codes, caja_id)

        # Agregar los códigos de las carpetas existentes a la lista
        if existing_carpetas_data:
            existing_carpetas = [carpeta.code for carpeta in existing_carpetas_data]

        return existing_carpetas
    
    def get_existing_carpetas(self, codes: List[str], caja_id: int) -> List[str]:
        existing_carpetas = []

        # Obtener todas las carpetas existentes para la caja_id dada
        existing_carpetas_data, _, _ = self.carpeta_data_access.get_existing_carpetas_data(codes, caja_id)

        # Agregar los códigos de las carpetas existentes a la lista
        if existing_carpetas_data:
            existing_carpetas = [carpeta.code for carpeta in existing_carpetas_data]

        return existing_carpetas
    
    def create_multiple_carpetas(self, carpeta_data: MultipleCarpetasCreate, current_user: dict):
        new_carpetas = []

        # Verificar si cada carpeta ya existe en la base de datos
        for code in carpeta_data.codes:
            if self.carpeta_data_access.carpeta_exists_by_code(code):
                return [], 0, 200, f"La carpeta con el código '{code}' ya existe"
            
            # Si no existe, agregarla a la lista de nuevas carpetas
            new_carpetas.append(code)

        # Insertar las nuevas carpetas
        for code in new_carpetas:
            new_carpeta = CarpetaModel(code=code, caja_id=carpeta_data.caja_id)
            new_carpeta.createUser=current_user.get('username')
            _, _, status_code, message = self.create_carpeta(new_carpeta)
            if status_code != 200:
                return [], 0, status_code, f"Error al insertar la carpeta con código '{code}': {message}"
        
        return [], 0, 200, "Success"
    

    def delete_carpeta(self, carpeta_id: int,user: str):
        
        response = self.carpeta_data_access.delete_carpeta(carpeta_id,user)
        log_id, status_code, msg = response

        return log_id, status_code, msg
    
    def get_carpetas_by_fecha(self, fecha_inicio: date, fecha_fin: date):
        return self.carpeta_data_access.get_carpetas_by_fecha(fecha_inicio, fecha_fin)
    
    def get_total_carpetas_by_caja_id(self, caja_id: int):

        response = self.carpeta_data_access.get_total_carpetas_by_caja_id(caja_id)

        print("response-response:",response)
        

        return response,0, 200, ""
    

       
    def get_all_carpetas_by_caja_id(self, caja_id: int):
        response = self.carpeta_data_access.get_all_carpetas_by_caja_id(caja_id)

        # Verificar si hay carpetas en la respuesta
        if response:
            # Si hay carpetas, convertirlas en formato de diccionario
            carpetas_list = [carpeta.dict() for carpeta in response[0]]
            return carpetas_list, 0, 200, "Carpetas retrieved by caja ID"
        else:
            # Si no hay carpetas, devolver un mensaje de error
            return [], 0, 200, "No hay carpetas asociadas a esta caja"

 



        


                    
        
