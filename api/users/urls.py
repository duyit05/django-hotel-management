from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.users.views import UserViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r'auth', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]