from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from AppleApp.models import LoginUser
from AppleApp.serializers.loginUser import LoginUserSerializer


class LoginUserApi(APIView):
    @staticmethod
    def get(request):
        data = LoginUser.custom_objects.all()
        serializer = LoginUserSerializer(many=True)
        serializer.instance = data
        serialized_data = serializer.data
        return Response(serialized_data)