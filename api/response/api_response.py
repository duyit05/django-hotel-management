from functools import wraps

from rest_framework.response import Response
from rest_framework import status as http_status

def api_response(success_message="Success"):
    """
    Decorator để wrap view DRF thành JSON chuẩn:
    {
        status: HTTP status code,
        message: "some message",
        data: ...
    }
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            # Nếu view đã trả Response rồi, không xử lý lại
            if isinstance(result, Response):
                return result

            # Nếu view trả dữ liệu, wrap thành JSON
            return Response({
                "status": http_status.HTTP_200_OK,
                "message": success_message,
                "data": result
            }, status=http_status.HTTP_200_OK)
        return wrapper
    return decorator