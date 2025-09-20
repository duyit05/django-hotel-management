from rest_framework.response import Response


def APIResponse(data=None, message='', status=200, extra=None):
    response_data = {
        'code': status,
        'message': message,
        'data': data
    }
    # merge các field ngoài data
    if extra:
        response_data.update(extra)
    return Response(response_data, status=status)


def APIError(message='', status=200):
    response_data = {
        'code': status,
        'message': message,
    }
    return Response(response_data, status=status)
