# user_router.py
from fastapi import APIRouter, Depends
from models.user import User as userModel
from models.user import UserInDB

from controllers import user_controller
from functions.dependencies import get_current_user
from typing import List


router = APIRouter()

@router.post("/user", tags=["User"])
def create_user(user_data: userModel, current_user: dict = Depends(get_current_user)):
    return user_controller.create_user(user_data)

@router.put("/user/{user_id}", tags=["User"])
def update_user(user_id: int, user: userModel, current_user: dict = Depends(get_current_user)):
    return user_controller.update_user(user_id, user)

@router.get("/users", tags=["User"], response_model=List[UserInDB])
def get_all_users(current_user: dict = Depends(get_current_user)):
    return user_controller.get_all_users()

@router.get("/user/{user_id}", tags=["User"])
def get_user_by_id(user_id: int, current_user: dict = Depends(get_current_user)):
    return user_controller.get_user_by_id(user_id)

@router.delete("/user/{user_id}", tags=["User"])
def delete_user(user_id: int, current_user: dict = Depends(get_current_user)):
    return user_controller.delete_user(user_id)  