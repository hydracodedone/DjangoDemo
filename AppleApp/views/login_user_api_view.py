import traceback

from rest_framework.response import Response
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.views import APIView

from AppleApp.modelAction.login_user_action_set import LoginModelAction
from AppleApp.serializers.login_user_serializer import LoginUserListlSerializer, \
    LoginUserCreateSerializer, LoginUserUpdateSerializer
from AppleApp.util.util import get_final_response


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
        try:
            data = request.data
            serializer = LoginUserCreateSerializer(many=False, data=data)
            if serializer.is_valid():
                LoginModelAction.create_new_user(**serializer.validated_data)
            return Response(serializer.errors)
        except Exception as err:
            print(traceback.format_exc())
            return Response(get_final_response(err), status=HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def put(request):
        data = request.data
        serializer = LoginUserUpdateSerializer(many=False, data=data)
        if serializer.is_valid():
            LoginModelAction.update_user(**serializer.validated_data)
        return Response(serializer.errors)
