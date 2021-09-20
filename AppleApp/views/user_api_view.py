from rest_framework.response import Response
from rest_framework.views import APIView

from AppleApp.model_action.login_user_action_set import LoginModelAction
from AppleApp.serializers.login_user_serializer import LoginUserCreateSerializer, LoginUserUpdateSerializer
from FirstProject.util.customized_authentication_permission.custom_authentication import JWTAutentication, \
    custom_authentication_decorator
from FirstProject.util.customized_authentication_permission.custom_permission import custom_permission_decorator, \
    CustomTestPermission
from FirstProject.util.customized_response.global_response import ResponseFomatter, MODIFY, ADD


class LoginUserApi(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serializer = LoginUserCreateSerializer(many=False, data=data)
        if serializer.is_valid():
            LoginModelAction.create_new_user(**serializer.validated_data)
        else:
            response_data = ResponseFomatter.get_validated_error(serializer.errors)
            return Response(response_data)
        response_data = ResponseFomatter.get_normal_response(ADD)
        return Response(response_data)

    @staticmethod
    @custom_authentication_decorator((JWTAutentication,))
    @custom_permission_decorator((CustomTestPermission,))
    def put(request):
        user_uid = request.user.uid
        data = request.data
        serializer = LoginUserUpdateSerializer(many=False, data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            validated_data.update(**{"uid": user_uid})
            LoginModelAction.update_user(**validated_data)
        else:
            response_data = ResponseFomatter.get_validated_error(serializer.errors)
            return Response(response_data)
        response_data = ResponseFomatter.get_normal_response(MODIFY)
        return Response(response_data)
