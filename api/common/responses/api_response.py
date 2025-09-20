from functools import wraps

from rest_framework.response import Response
from rest_framework import status as http_status


def api_response(success_message="Success"):
    """
    Decorator để wrap view DRF thành JSON chuẩn.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if isinstance(result, Response):
                return result

            return Response({
                "status": http_status.HTTP_200_OK,
                "message": success_message,
                "data": result
            }, status=http_status.HTTP_200_OK)
        return wrapper
    return decorator




