# functions/api_response.py
from fastapi.responses import JSONResponse
from fastapi import status
from dataAccess.moduloInventario import LogDataAccess

class ApiResponse:
    @staticmethod
    def success(data, message=None, status_code=200):
        return JSONResponse(
            status_code=status_code,
            content={
                "data": data,
                "message": message,
                "status": "success" 
            }
        )

    @staticmethod
    def error(message, log_id=None, status_code=500):
        log_data_access = LogDataAccess()

        if(status_code==500):
            return JSONResponse(
                status_code=status_code,
                content={
                    "data": None,
                    "message": "Algo ocurrio",
                    "error": {"folio_error": log_id},
                    "status": "error" 
                })
        elif(status_code==409):
            log_id = log_data_access.log_error(message)
            return JSONResponse(
                status_code=status_code,
                content={
                    "data": [],
                    "message":"Algo ocurrio", 
                    "error": {"folio_error": log_id, "details":message },
                    "status": "error" 
                })
        else:
            return JSONResponse(
                status_code=status_code,
                content={
                    "data": None,
                    "message": message,
                    "status": "success"
                })
        
        
 
