# routers/auth_router.py
from fastapi import APIRouter, Form, Depends
from controllers import auth_controller
from functions.dependencies import get_current_user
from functions.response_descriptions import response_descriptions


router = APIRouter()

@router.post("/login", tags=["Auth"],  responses=response_descriptions)
def login(username: str = Form(...), password: str = Form(...)):
    return auth_controller.login(username, password)

@router.post("/token/refresh", tags=["Auth"], responses=response_descriptions) 
def refresh_token(current_user: dict = Depends(get_current_user)):
    print("current_user-current_user",current_user)
    return auth_controller.refresh_token(current_user) 
