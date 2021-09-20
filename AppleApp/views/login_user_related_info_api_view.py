from drf_yasg2.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from AppleApp.model_action.login_user_related_info_management import LoginUserRelatedAction
from AppleApp.serializers.login_user_related_info_serializer import UserRelatedInfoSerializer
from FirstProject.util.customized_response.global_response import ResponseFomatter


class UserRelatedInfoAPIView(APIView):
    @staticmethod
    @swagger_auto_schema(
        security=[],
        operation_description="查询用户相关常量信息",
    )
    def get(request):
        data = LoginUserRelatedAction.query_login_user_related_info()
        serializer = UserRelatedInfoSerializer(many=False)
        serializer.instance = data
        response_data = ResponseFomatter.get_normal_response(serializer.data)
        return Response(response_data)
