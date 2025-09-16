from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.models import Room
from api.serialazer import RoomSerializer


# Create your views here.
@api_view(['GET'])
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
    return get_object_or_404(Room, room_id = room_id)


@api_view(['GET'])
def get_detail_room(request, room_id):
    room = get_room_by_id(room_id = room_id)
    serializer = RoomSerializer(room)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_room (request,room_id):
    room = get_room_by_id(room_id = room_id)
    room.delete()
    return Response(status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def update_room (request, room_id):
    room = get_room_by_id(room_id)
    serializer = RoomSerializer(room, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
    return Response(serializer.data)
