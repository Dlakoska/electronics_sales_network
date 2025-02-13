from rest_framework import permissions


class IsActiveAuthenticatedUser(permissions.BasePermission):
    """Проверка является ли пользователь аутентифицированным и активным"""
    def has_permission(self, request, view):
        return request.user and request.user.is_active and request.user.is_authenticated
