from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from api.constrants.api_constraint import APIMessage
from api.exceptions.api_exception import AppException
from api.response.api_response import api_response
from api.serializers.user_serializer import UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
@api_response(success_message='register user')
def register(request):
    user = UserSerializer(data=request.data)
    user.is_valid(raise_exception=True)
    user.save()
    return user.data

@api_view(['POST'])
@permission_classes([AllowAny])
def login (request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
       raise AppException(APIMessage.USERNAME_OR_PASSWORD_BLANK)

    # authenticate
    user = authenticate(username = username, password = password)
    if user is None:
        raise AppException(APIMessage.USERNAME_OR_PASSWORD_INCORRECT)

    # sinh token
    refresh_token = RefreshToken.for_user(user)
    roles = [g.name for g in user.groups.all()]

    refresh_token['username'] = user.username
    refresh_token['roles'] = roles

    return Response({
        'access_token': str(refresh_token.access_token),
        'refresh_token': str(refresh_token),
        'username': user.name,
        'roles': roles
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@api_response(success_message='get my info')
def get_info(request):
    user = request.user
    serializer = UserSerializer(user)
    return serializer.data

