from fastapi import HTTPException
from models.user import User as userModel
from business.moduloInventario import UserBusiness
from functions.api_response import ApiResponse

user_business = UserBusiness()

def create_user(user_data: userModel):

    response = user_business.create_user(user_data)

    user_id, log_id, status_code,msg = response
    if user_id:
        return ApiResponse.success({"user_id": user_id}, msg)
    else:
        return ApiResponse.error(msg, log_id,status_code)

def update_user(user_id: int, user: userModel):

    result, message, status_code = user_business.update_user(user_id, user)
    if result is not None:
        return {"message": message, "user_id": result}
    else:
        return HTTPException(status_code=status_code, detail=message)
    
def get_user_by_id(user_id: int):
    try:
        response =user_business.get_user_by_id(user_id)
        data, log_id, status_code,msg = response
        if data:
            return ApiResponse.success({"user": data.dict()}, msg)
        else:
            return ApiResponse.error(msg, log_id,status_code) 
    except Exception as e:
        print("Exception",e)
        return ApiResponse.error(str(e), 0,409)
    
def get_all_users():
    try:
        response = user_business.get_all_users()
        print("get_all_users-response", response)
        data, log_id, status_code, msg = response

        if data:
            # Convertir cada objeto UserInDB en un diccionario
            users_list = [user.dict() for user in data]
            return ApiResponse.success({"users": users_list}, msg)
        else:
            return ApiResponse.error(msg, log_id, status_code) 
    except Exception as e:
        print("Exception", e)
        return ApiResponse.error(str(e), 0, 409)
    
def delete_user(user_id: int):
    try:
        response = user_business.delete_user(user_id)
        log_id, status_code, msg = response

        if status_code == 200:
            return ApiResponse.success({"user_id": user_id}, msg)
        else:
            return ApiResponse.error(msg, log_id, status_code)
    except Exception as e:
        print("Exception", e)
        return ApiResponse.error(str(e), 0, 409)   

