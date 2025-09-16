from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from api.models import Room
from api.permissions import IsAdmin
from api.serialazer import RoomSerializer, UserSerializer


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAdmin])
def get_list_room(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_room(request):
    serializer = RoomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_room_by_id(room_id):
    return get_object_or_404(Room, room_id=room_id)


@api_view(['GET'])
def get_detail_room(request, room_id):
    room = get_room_by_id(room_id=room_id)
    serializer = RoomSerializer(room)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_room(request, room_id):
    room = get_room_by_id(room_id=room_id)
    room.delete()
    return Response(status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def update_room(request, room_id):
    room = get_room_by_id(room_id)
    serializer = RoomSerializer(room, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])  # permits all
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])  # Cho phép ai cũng gọi được
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': "username or password is not blank"}, status=status.HTTP_400_BAD_REQUEST)

    # xác thực user
    user = authenticate(username=username, password=password)
    if user is None:
        return Response({'error': 'username or password incorrect'})

    # Sinh token và refresh
    refresh_token = RefreshToken.for_user(user)
    roles = [g.name for g in user.groups.all()]

    refresh_token['username'] = user.username
    refresh_token['roles'] = roles

    return Response({
        "access_token": str(refresh_token.access_token),  # để access trước
        "refresh_token": str(refresh_token),
        "username" : user.username,
        "roles": roles
    }, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_my_info(request):
    user = request.user
    return Response({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "name": user.get_full_name(),
        "roles": [g.name for g in user.groups.all()]
    })
