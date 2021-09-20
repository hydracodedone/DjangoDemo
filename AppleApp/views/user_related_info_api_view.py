from drf_yasg2.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from AppleApp.model_action.onwer_type_action_set import OwnerTypeModelAction
from AppleApp.serializers.onwer_type_serializer import OwnerTypeSerializer
from FirstProject.util.customized_response.global_response import ResponseFomatter


class UserRelatedInfoAPIView(APIView):
    @staticmethod
    @swagger_auto_schema(
        security=[],
        operation_description="查询用户相关常量信息",
    )
    def get(request):
        data = OwnerTypeModelAction.get_all_data()
        serializer = OwnerTypeSerializer(many=True)
        serializer.instance = data
        response_data = ResponseFomatter.get_normal_response(serializer.data)
        return Response(response_data)
