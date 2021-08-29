from rest_framework.response import Response
from rest_framework.views import APIView

from AppleApp.model_action.login_user_action_set import LoginModelAction
from AppleApp.serializers.login_user_serializer import LoginUserCreateSerializer, LoginUserUpdateSerializer
from FirstProject.util.constant.stand_response import STAND_RESPONSE


class LoginUserApi(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serializer = LoginUserCreateSerializer(many=False, data=data)
        if serializer.is_valid():
            LoginModelAction.create_new_user(**serializer.validated_data)
        else:
            return Response(serializer.errors)
        return Response(STAND_RESPONSE)

    @staticmethod
    def put(request):
        data = request.data
        serializer = LoginUserUpdateSerializer(many=False, data=data)
        if serializer.is_valid():
            LoginModelAction.update_user(**serializer.validated_data)
        else:
            return Response(serializer.errors)
        return Response(STAND_RESPONSE)
