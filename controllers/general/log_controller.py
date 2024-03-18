# controllers/general/log_controller.py
from business.BU_Log import LogBusiness
from functions.api_response import ApiResponse

BU = LogBusiness()

def get_logs():
    logs_data = BU.get_all_logs()
    return ApiResponse.success(logs_data, "Logs fetched successfully")
 