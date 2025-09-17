from rest_framework.permissions import BasePermission

from api.enums.user_role import UserRole


class IsAdmin(BasePermission):
    # Cho phép truy cập nếu user thuộc group 'ADMIN'
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name=UserRole.ADMIN).exists()
