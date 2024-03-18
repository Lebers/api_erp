# business/business_logic.py
from dataAccess.moduloInventario import ModuloInventario_DataAccess as MI_DataAccess

_DA = MI_DataAccess()

class LogBusiness:
 
    def get_all_logs(self):
        response = _DA.get_all_logs()
        
        return response
 