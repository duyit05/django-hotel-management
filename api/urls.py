from django.urls import path
from .views.room_view import get_all_room, create_room, get_detail_room, delete_room, update_room
from .views.user_view import register,login,get_info
urlpatterns = [
    path('rooms', get_all_room),
    path('room/create', create_room),
    path('room/detail/<int:room_id>', get_detail_room),
    path('room/delete/<int:room_id>', delete_room),
    path('room/update/<int:room_id>', update_room),

    # USER
    path('register', register),
    path('login', login),
    path('my-info', get_info)

]
