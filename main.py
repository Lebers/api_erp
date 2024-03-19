import uvicorn
from fastapi import FastAPI, Request, HTTPException
from routers.general import log_router
from routers.moduloInventario import carpeta_router,  reporte_router, user_router, caja_router,auth_router
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from dataAccess.moduloInventario import LogDataAccess
from fastapi.middleware.cors import CORSMiddleware

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

# Include routers from imported modules
app.include_router(auth_router.router)
app.include_router(user_router.router)
app.include_router(caja_router.router)
app.include_router(carpeta_router.router)
app.include_router(reporte_router.router)
app.include_router(log_router.router)


def serve():
    
    uvicorn.run(app, host="127.0.0.1", port=8004)  


if __name__ == "__main__":
    serve()

  

