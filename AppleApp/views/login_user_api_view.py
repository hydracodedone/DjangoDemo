from rest_framework.response import Response
from rest_framework.views import APIView

from AppleApp.model_action.login_user_action_set import LoginModelAction
from AppleApp.serializers.login_user_serializer import LoginUserCreateSerializer, LoginUserUpdateSerializer, \
    LoginUserLoginSerializer
from AppleApp.serializers.token_serializer import TokenSerializer
from FirstProject.util.customized_authentication_permission.token_manager import UserLoginJWTAuthentication
from FirstProject.util.customized_response.global_response import ResponseFomatter


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
        response_data = ResponseFomatter.get_normal_response(serializer.data)
        return Response(response_data)

    @staticmethod
    def put(request):
        data = request.data
        serializer = LoginUserUpdateSerializer(many=False, data=data)
        if serializer.is_valid():
            LoginModelAction.update_user(**serializer.validated_data)
        else:
            response_data = ResponseFomatter.get_validated_error(serializer.errors)
            return Response(response_data)
        response_data = ResponseFomatter.get_normal_response(serializer.data)
        return Response(response_data)


class TokenGenerageAPIView(APIView):
    @staticmethod
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


class TokenRefreshAPIView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serializer = TokenSerializer(many=False, data=data)
        if serializer.is_valid():
            token = UserLoginJWTAuthentication.refresh_token(**serializer.validated_data)
            response_data = ResponseFomatter.get_normal_response(token)
        else:
            response_data = ResponseFomatter.get_validated_error(serializer.errors)
        return Response(response_data)
