import uvicorn
from fastapi import FastAPI, Request, HTTPException
from routers.general import log_router
from routers.moduloInventario import carpeta_router,  reporte_router, user_router, caja_router,auth_router
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from dataAccess.moduloInventario import LogDataAccess
from fastapi.middleware.cors import CORSMiddleware
import socket
from dotenv import load_dotenv
from router_config import include_routers


import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],   
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    log_data_access = LogDataAccess()
    errors = []
    error_messages = []

    for error in exc.errors():
        loc = ".".join(error['loc']) if isinstance(error['loc'], list) else str(error['loc'])
        error_message = f"Field '{loc}' is required"
        errors.append({
            "type": error['type'],
            "loc": loc,
            "msg": error_message,
        })
        error_messages.append(error_message)
    
    full_error_message = "; ".join(error_messages)
    log_id = log_data_access.log_error(full_error_message)

    return JSONResponse(
        status_code=422,
        content={
            "data": None,
            "message": "Validation error",
            "error": {
                "details": errors,
                "folio": log_id   
            }  
        }
    )
@app.exception_handler(HTTPException)
def http_exception_handler(request, exc):
    if exc.detail == "Not authenticated":
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "data": None,
                "message": "No autenticado",
                "error": str(exc.detail)
            }
        )
    # Puedes manejar otros tipos de HTTPException aquí
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "data": None,
            "message": "Error HTTP",
            "error": str(exc.detail)
        }
    )

# Include routers
include_routers(app)


def get_host_ip():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return host_ip
    except:
        return "127.0.0.1"

def serve():
    # Decide si usar la IP dinámica o la estática basándose en la variable de entorno
    use_dynamic_ip = os.getenv("USE_DYNAMIC_IP", "false").lower() == "true"
    host_ip = get_host_ip() if use_dynamic_ip else "127.0.0.1"
    server_port = int(os.getenv('SERVER_PORT', 8004))  # Usa 8004 como puerto predeterminado si no se especifica

    uvicorn.run(app, host=host_ip, port=server_port)

if __name__ == "__main__":
    serve()

 