# business/moduloInventario.py
from dataAccess.CajaDataAccess import CajaDataAccess
from models.caja import Caja as CajaModel
from models.caja import Cajaxxx
from datetime import date


caja_data_access = CajaDataAccess()

class CajaBusiness:
    def create_caja(self, caja: CajaModel):
        try:
            if caja_data_access.caja_exists(caja.code):
                return None, None, 400, "Caja already exists"
            response = caja_data_access.create_caja(caja)
            caja_id, log_id, *rest = response
            status_code = rest[0] if rest else 200
            return caja_id, log_id, status_code, "Caja created"
        except Exception as e:
            print("Exception", e)
            return None,0,409, str(e)+"/CajaBusiness/create_caja"

    def update_caja(self, caja_id: int, caja: CajaModel):
        try:
            # Verifica si el caja_id existe
            if not caja_data_access.caja_exists_by_id(caja_id):
                return None, None, 400, "Id de Caja no existe"  # Retorna un error 404 si el caja_id no existe
                
            # Verifica si el código de la caja ya existe en otra caja
            if caja_data_access.caja_exists(caja.code):
                return None, None, 400, "codigo de caja ya existe"  # Retorna un error de conflicto (409)
            
            # Si el código no existe en otra caja, procede con la actualización
            response = caja_data_access.update_caja(caja_id, caja)
            caja_id, log_id, *rest = response
            status_code = rest[0] if rest else 200
            return caja_id, log_id, status_code, "Caja updated"
        except Exception as e:
            print("Exception", e)
            return None,0,409, str(e)+"/CajaBusiness/create_caja"

    def get_all_cajas(self):
        response = caja_data_access.get_all_cajas()
        data, log_id, *rest = response
        status_code = rest[0] if rest else 200
        return data, log_id, status_code, "Caja data"

    def get_caja_by_id(self, caja_id: int):
        response = caja_data_access.get_caja_by_id(caja_id)
        data, log_id, *rest = response
        status_code = rest[0] if rest else 200
        return data, log_id, status_code, "Caja data"

    def delete_caja(self, caja_id: int,user: str):
        
        print("user-user:",user)
        response = caja_data_access.delete_caja(caja_id,user)
        log_id, status_code, msg = response

        return log_id, status_code, msg
    
    def get_cajas_by_fecha(self, fecha_inicio: date, fecha_fin: date):
        return caja_data_access.get_cajas_by_fecha(fecha_inicio, fecha_fin)
