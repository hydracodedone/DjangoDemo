from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from AppleApp.serializers.token_serializer import TokenSerializer
from FirstProject.util.customized_authentication_permission.token_manager import UserLoginJWTAuthentication


class JWTAutentication(BaseAuthentication):
    def authenticate(self, request):
        serializer = TokenSerializer(many=False, data=request.data)
        if serializer.is_valid():
            user_instance = UserLoginJWTAuthentication.revify_token(serializer.validated_data.get("token"))
            return user_instance, True
        else:
            raise exceptions.AuthenticationFailed(serializer.errors)

