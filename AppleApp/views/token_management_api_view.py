from drf_yasg2.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from AppleApp.model_action.login_user_management import LoginModelAction
from AppleApp.serializers.login_user_serializer import LoginUserLoginSerializer
from AppleApp.serializers.token_serializer import TokenSerializer
from FirstProject.util.customized_authentication_permission.token_manager import UserLoginJWTAuthentication
from FirstProject.util.customized_response.global_response import ResponseFomatter


class TokenManagementAPIView(APIView):
    @staticmethod
    @swagger_auto_schema(
        security=[],
        operation_description="token获取",
    )
    def post(request):
        data = request.data
        serializer = LoginUserLoginSerializer(many=False, data=data)
        if serializer.is_valid():
            user_data = LoginModelAction.query_user_by_login_user_name_and_password(**serializer.validated_data)
            token = UserLoginJWTAuthentication.generate_token(user_data)
            response_data = ResponseFomatter.get_normal_response(token)
        else:
            response_data = ResponseFomatter.get_validated_error(serializer.errors)
        return Response(response_data)

    @staticmethod
    @swagger_auto_schema(
        security=[],
        operation_description="token更新",
    )
    def put(request):
        data = request.data
        serializer = TokenSerializer(many=False, data=data)
        if serializer.is_valid():
            token = UserLoginJWTAuthentication.refresh_token(**serializer.validated_data)
            response_data = ResponseFomatter.get_normal_response(token)
        else:
            response_data = ResponseFomatter.get_validated_error(serializer.errors)
        return Response(response_data)
