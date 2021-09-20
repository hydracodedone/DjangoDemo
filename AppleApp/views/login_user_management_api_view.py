from drf_yasg2.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from AppleApp.model_action.login_user_management import LoginModelAction
from AppleApp.serializers.login_user_serializer import LoginUserCreateSerializer, LoginUserUpdateSerializer
from FirstProject.util.customized_authentication_permission.custom_authentication import JWTAutentication, \
    custom_authentication_decorator
from FirstProject.util.customized_authentication_permission.custom_permission import custom_permission_decorator, \
    CustomTestPermission
from FirstProject.util.customized_response.global_response import ResponseFomatter, MODIFY, ADD


class LoginUserApi(APIView):
    @staticmethod
    @swagger_auto_schema(
        security=[],
        operation_description="用户注册",
    )
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
    @swagger_auto_schema(
        security=[],
        operation_description="用户修改",
    )
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
