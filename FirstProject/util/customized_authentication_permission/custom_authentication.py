from rest_framework.authentication import BaseAuthentication

from AppleApp.model_action.permission_action_set import PermissionActionSet
from FirstProject.util.customized_authentication_permission.token_manager import UserLoginJWTAuthentication


class JWTAutentication(BaseAuthentication):
    def authenticate(self, request):
        token_encrypt = request.POST.get("token")
        user_instance = UserLoginJWTAuthentication.revify_token(token_encrypt)
        return user_instance, PermissionActionSet.get_specific_permission(user_instance)
