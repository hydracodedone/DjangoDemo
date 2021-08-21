import traceback

from rest_framework.response import Response
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.views import APIView

from AppleApp.modelAction.login_user_action_set import LoginModelAction
from AppleApp.models import LoginUser
from AppleApp.serializers.login_user_serializer import LoginUserSerializer
from AppleApp.util.util import get_final_response


class LoginUserApi(APIView):
    @staticmethod
    def get(request):
        data = LoginUser.custom_objects.all()
        serializer = LoginUserSerializer(many=True)
        serializer.instance = data
        serialized_data = serializer.data
        return Response(serialized_data)

    @staticmethod
    def post(request):
        try:
            data = request.data
            serializer = LoginUserSerializer(many=False, data=data)
            if serializer.is_valid():
                LoginModelAction.create_new_user(**serializer.validated_data)
            return Response(serializer.errors)
        except Exception as err:
            print(traceback.format_exc())
            return Response(get_final_response(err), status=HTTP_500_INTERNAL_SERVER_ERROR)
