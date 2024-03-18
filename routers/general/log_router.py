# routers/general/log_router.py
from fastapi import APIRouter
from typing import List
from models.log_Model import Log
from controllers.general import log_controller

router = APIRouter()

@router.get("/logs", tags=["Logs"] )
def get_logs():
    return log_controller.get_logs()

@router.get("/logs/{log_id}", tags=["Logs"], response_model=Log)
def get_log(log_id: int):
    return log_controller.get_log(log_id)
