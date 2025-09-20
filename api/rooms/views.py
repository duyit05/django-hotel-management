from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import ViewSet

from api.common.pagination import Pagination
from api.constants.custom_reponse import APIResponse, APIError
from api.config.permission.permissions import IsAdmin
from api.rooms.models import Room
from api.rooms.serializers import RoomSerializer


class RoomViewSet(ViewSet):

    @action(detail=False,methods=['GET'],url_path='list', permission_classes=[AllowAny])
    def get_list_room(self,request):
        rooms = Room.objects.all()
        # PAGING
        paginator = Pagination()
        pagination = paginator.paginate_queryset(rooms, request)
        serializer = RoomSerializer(pagination, many = True)

        return paginator.get_paginated_response(serializer.data,message="get all rooms successfully")


    @action(detail=False, methods=['POST'],url_path='create', permission_classes=[IsAdmin])
    def create_room(self,request):
        print(f"Admin: {IsAdminUser}" )
        room = RoomSerializer(data= request.data)
        room.is_valid(raise_exception=True)
        room.save()
        return APIResponse(room.data, 'create room success', status.HTTP_201_CREATED)

    @action(detail=True, methods=['DELETE'],url_path='delete',permission_classes=[AllowAny])
    def delete_room(self,request,pk):
        room = get_object_or_404(Room, pk = pk)
        room.delete()
        return APIResponse('delete room success', status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['PUT'],url_path='update', permission_classes=[AllowAny])
    def update_room(self,request, pk):
        room = get_object_or_404(Room, pk = pk)
        serializer = RoomSerializer(room, data = request.data)
        if serializer.is_valid(raise_exception=True):
             return APIResponse(serializer.data, 'update room success', status.HTTP_202_ACCEPTED)
        return APIError('update room fail', status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['GET'],url_path='detail', permission_classes=[AllowAny])
    def get_detail_room(self,request,pk):
        room = get_object_or_404(Room,pk = pk)
        serializer = RoomSerializer(room)
        return APIResponse(serializer.data,'get detail room', status.HTTP_200_OK)
