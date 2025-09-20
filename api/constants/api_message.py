from rest_framework import status


class APIMessage:
    # (message, http_status)
    USERNAME_OR_PASSWORD_BLANK = ("Username or password cannot be blank",status.HTTP_400_BAD_REQUEST)
    USER_NOT_FOUND = ("User not found", status.HTTP_404_NOT_FOUND)
    USERNAME_OR_PASSWORD_INCORRECT = ("Username or password incorrect",status.HTTP_400_BAD_REQUEST)


