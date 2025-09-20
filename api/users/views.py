from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from api.constants.api_message import APIMessage
from api.constants.custom_reponse import APIResponse, APIError
from api.common.exceptions.api_exception import AppException
from api.users.serializers import UserSerializer


class UserViewSet(ViewSet):

    @action(detail=False, methods=["GET"],url_path='my-info', permission_classes=[IsAuthenticated])
    def me(self, request):
        serializer = UserSerializer(request.user)
        return APIResponse(serializer.data, 'get my info', status.HTTP_200_OK)

    # -------- REGISTER --------
    @action(detail=False, methods=["POST"], url_path='register',permission_classes=[AllowAny])
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return APIResponse(serializer.data, 'register user', status.HTTP_200_OK)
        return APIError('register fail', status.HTTP_400_BAD_REQUEST)

    # -------- LOGIN --------
    @action(detail=False, methods=["POST"],url_path='login', permission_classes=[AllowAny])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            raise AppException(APIMessage.USERNAME_OR_PASSWORD_BLANK)

        user = authenticate(username=username, password=password)
        if user is None:
            raise AppException(APIMessage.USERNAME_OR_PASSWORD_INCORRECT)

        refresh_token = RefreshToken.for_user(user)
        roles = [g.name for g in user.groups.all()]
        refresh_token['username'] = user.username
        refresh_token['roles'] = roles

        return Response({
            'access_token': str(refresh_token.access_token),
            'refresh_token': str(refresh_token),
            'username': user.username,
            'roles': roles
        }, status=status.HTTP_200_OK)
