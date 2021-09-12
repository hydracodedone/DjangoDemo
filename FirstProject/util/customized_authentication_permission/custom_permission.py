from rest_framework.permissions import BasePermission


class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        if request._request.get_full_path not in request.auth:
            return False
        else:
            return True

    def has_object_permission(self, request, view, obj):
        pass
