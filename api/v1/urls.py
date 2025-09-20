from django.urls import include, path

urlpatterns = [
    path('', include('api.users.urls')),
    path('', include('api.rooms.urls')),
]


