from rest_framework.response import Response
from rest_framework.views import APIView

from AppleApp.model_action.login_user_action_set import LoginModelAction
from AppleApp.serializers.login_user_serializer import LoginUserCreateSerializer, LoginUserUpdateSerializer
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
