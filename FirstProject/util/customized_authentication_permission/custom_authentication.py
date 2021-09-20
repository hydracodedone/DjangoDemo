from functools import update_wrapper

from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from AppleApp.serializers.token_serializer import TokenSerializer
from FirstProject.util.customized_authentication_permission.token_manager import UserLoginJWTAuthentication


class JWTAutentication(BaseAuthentication):
    def authenticate(self, request):
        if request.method.upper() != "GET":
            token_data = request.data
        else:
            token_data = request.query_params
        serializer = TokenSerializer(many=False, data=token_data)
        if serializer.is_valid():
            user_instance = UserLoginJWTAuthentication.revify_token(serializer.validated_data.get("token"))
            return user_instance, True
        else:
            raise exceptions.AuthenticationFailed(serializer.errors)


def custom_authentication_decorator(authentication_classes):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            request.authenticators.extend([x() for x in authentication_classes])
            request._authenticate()
            return func(request, *args, **kwargs)

        return update_wrapper(wrapper, func)

    return decorator
