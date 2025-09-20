from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.rooms.views import RoomViewSet

router = SimpleRouter(trailing_slash=False)  # bỏ dấu /
router.register(r'room', RoomViewSet, basename='room')

urlpatterns = [
    path('', include(router.urls)),
]