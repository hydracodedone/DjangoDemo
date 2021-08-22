from rest_framework.response import Response
from rest_framework.views import APIView

from AppleApp.modelAction.login_user_action_set import LoginModelAction
from AppleApp.serializers.login_user_serializer import LoginUserListlSerializer, \
    LoginUserCreateSerializer, LoginUserUpdateSerializer


class LoginUserApi(APIView):
    @staticmethod
    def get(request):
        data = LoginModelAction.query_all_user_with_owner_info()
        serializer = LoginUserListlSerializer(many=True)
        serializer.instance = data
        serialized_data = serializer.data
        return Response(serialized_data)

    @staticmethod
    def post(request):
        data = request.data
        serializer = LoginUserCreateSerializer(many=False, data=data)
        if serializer.is_valid():
            LoginModelAction.create_new_user(**serializer.validated_data)
        return Response(serializer.errors)

    @staticmethod
    def put(request):
        data = request.data
        serializer = LoginUserUpdateSerializer(many=False, data=data)
        if serializer.is_valid():
            LoginModelAction.update_user(**serializer.validated_data)
        return Response(serializer.errors)
