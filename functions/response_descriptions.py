# response_descriptions.py

response_descriptions = {
    200: {
        "content": {
            "application/json": {
                "example": {
                    "data": "datos solicitados",
                    "message": "mensaje para el usuario final" 
                }
            }
        }
    },
    401: {
        "content": {
            "application/json": {
                "example": {
                    "data": [],
                    "message": "mensaje para el usuario final"
                }
            }
        }
    },
    422: {
        "content": {
            "application/json": {
                "example": {
                    "data": [],
                    "message": "mensaje para el usuario final",
                    "error": {
                        "details": "detalle del error",
                        "folio": "numero del folio en logs"
                    }
                }
            }
        }
    }
}
