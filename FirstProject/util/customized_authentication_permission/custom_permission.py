from functools import update_wrapper

from rest_framework import exceptions
from rest_framework.permissions import BasePermission
from rest_framework.request import Request

from AppleApp.model_action.permission_management import PermissionActionSet


class CustomPermission(BasePermission):
    def has_permission(self, request: Request, view):
        if not hasattr(request, "user"):
            raise exceptions.NotAuthenticated()
        if not hasattr(request, "auth"):
            raise exceptions.NotAuthenticated()
        if not request.auth:
            raise exceptions.NotAuthenticated()
        else:
            url_permission_set = PermissionActionSet.get_specific_permission(request.user)
            if request._request.get_full_path() not in url_permission_set:
                return False
            else:
                return True

    def has_object_permission(self, request, view, obj):
        pass


class CustomTestPermission(BasePermission):
    def has_permission(self, request: Request, view):
        if not hasattr(request, "user"):
            raise exceptions.NotAuthenticated()
        if not hasattr(request, "auth"):
            raise exceptions.NotAuthenticated()
        if not request.auth:
            raise exceptions.NotAuthenticated()
        else:
            return True


def custom_permission_decorator(permission_classes):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            for each_permission in permission_classes:
                result = each_permission().has_permission(request, None)
                if not result:
                    raise exceptions.PermissionDenied()
            return func(request, *args, **kwargs)

        return update_wrapper(wrapper, func)

    return decorator
