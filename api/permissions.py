from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    # Cho phép truy cập nếu user thuộc group 'ADMIN'
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='ADMIN').exists()
