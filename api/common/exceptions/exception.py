from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(response.data, dict):
            first_field = next(iter(response.data))
            first_msg = response.data[first_field]
            if isinstance(first_msg, list):
                first_msg = first_msg[0]
            response_data = {
                "status": response.status_code,
                "message": first_msg,
            }
            response.data = response_data
        else:
            response.data = {
                "status": response.status_code,
                "message": str(response.data),
            }
    return response




