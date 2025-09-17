from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.models import Room
from api.permissions import IsAdmin
from api.response.api_response import api_response
from api.serializers.room_serializer import RoomSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
@api_response(success_message='get all rooms')
def get_all_room(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return serializer.data


@api_view(['POST'])
@permission_classes([IsAdmin])
@api_response(success_message='create room')
def create_room(request):
    serializer = RoomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    return Response(status=status.HTTP_400_BAD_REQUEST)

def get_room_by_id (room_id):
    return get_object_or_404(Room, room_id = room_id)

@api_view(['GET'])
@permission_classes([AllowAny])
@api_response(success_message='get detail room')
def get_detail_room(request, room_id):
    room = get_room_by_id(room_id)
    serializer = RoomSerializer(room)
    return serializer.data

@api_view(['DELETE'])
@permission_classes([IsAdmin])
def delete_room(request, room_id):
    room = get_room_by_id(room_id)
    room.delete()
    return Response({'message': 'delete success'},status = status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
@permission_classes([IsAdmin])
@api_response(success_message='update room')
def update_room (request, room_id):
    room = get_room_by_id(room_id)
    serializer = RoomSerializer(room, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    return Response(status = status.HTTP_400_BAD_REQUEST)

