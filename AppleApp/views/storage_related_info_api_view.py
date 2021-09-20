from drf_yasg2.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from AppleApp.model_action.storge_info_action_set import StorageTypeModelAction
from AppleApp.serializers.storage_type_serializer import StorageRelatedInfoSerializer
from FirstProject.util.customized_authentication_permission.custom_authentication import JWTAutentication
from FirstProject.util.customized_authentication_permission.custom_permission import CustomTestPermission
from FirstProject.util.customized_response.global_response import ResponseFomatter


class StorageInfoAPIView(APIView):
    authentication_classes = [JWTAutentication]
    permission_classes = [CustomTestPermission]

    @staticmethod
    @swagger_auto_schema(
        security=[],
        operation_description="查询存储相关信息",
    )
    def get(request):
        data = StorageTypeModelAction.get_storage_info()
        serializer = StorageRelatedInfoSerializer(many=False)
        serializer.instance = data
        response_data = ResponseFomatter.get_normal_response(serializer.data)
        return Response(response_data)
