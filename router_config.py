# router_config.py
from fastapi import FastAPI
from routers.general import log_router
from routers.moduloInventario import carpeta_router, reporte_router, user_router, caja_router, auth_router

def include_routers(app: FastAPI):
    app.include_router(auth_router.router)
    app.include_router(user_router.router)
    app.include_router(caja_router.router)
    app.include_router(carpeta_router.router)
    app.include_router(reporte_router.router)
    app.include_router(log_router.router)
