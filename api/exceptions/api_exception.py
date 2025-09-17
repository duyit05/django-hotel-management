from rest_framework.exceptions import APIException


class AppException(APIException):
    def __init__(self, message_tuple):
        """
        message_tuple = (message:str, http_status_code:int)
        """
        self.detail = message_tuple[0]  # message
        self.status_code = message_tuple[1]  # HTTP status code