from drf_yasg2.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from AppleApp.model_action.storage_pool_related_info_management import StoragePoolRelatedInfoManagement
from FirstProject.util.customized_authentication_permission.custom_authentication import JWTAutentication
from FirstProject.util.customized_authentication_permission.custom_permission import CustomTestPermission
from FirstProject.util.customized_response.global_response import ResponseFomatter


class StoragePoolRelatedAPIView(APIView):
    authentication_classes = [JWTAutentication]
    permission_classes = [CustomTestPermission]

    @staticmethod
    @swagger_auto_schema(
        security=[],
        operation_description="查询存储库相关信息",
    )
    def get(request):
        data = StoragePoolRelatedInfoManagement().query_data()
        response_data = ResponseFomatter.get_normal_response(data)
        return Response(response_data)
