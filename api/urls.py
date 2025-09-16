from django.urls import path
from . import views

urlpatterns = [
    path('rooms', view=views.get_list_room),
    path('room/create', view=views.create_room),
    path('room/detail/<int:room_id>', view=views.get_detail_room),
    path('room/delete/<int:room_id>', view=views.delete_room),
    path('room/update/<int:room_id>', view=views.update_room),

    # USER
    path('register', view = views.register),
    path('login', view = views.login),
    path('my-info', view=views.get_my_info),

]
