# encoding=UTF-8
from drf_yasg2.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from AppleApp.model_action.adminstation_area_action_set import AdminstrativeDivisionAction
from AppleApp.serializers.administrative_division_serializer import AdministrativeDivisionSerializer
from FirstProject.util.customized_authentication_permission.custom_authentication import JWTAutentication, \
    custom_authentication_decorator
from FirstProject.util.customized_authentication_permission.custom_permission import CustomTestPermission, \
    custom_permission_decorator
from FirstProject.util.customized_response.global_response import ResponseFomatter


class AdministrativeDivisionAPIView(APIView):
    authentication_classes = [JWTAutentication]
    permission_classes = [CustomTestPermission]

    @staticmethod
    @swagger_auto_schema(
        security=[],
        operation_description="查询行政区域信息",
    )
    @custom_authentication_decorator((JWTAutentication,))
    @custom_permission_decorator((CustomTestPermission,))
    def get(request):
        data = AdminstrativeDivisionAction.query_all_administrative_data()
        serializer = AdministrativeDivisionSerializer(many=True)
        serializer.instance = data
        response_data = ResponseFomatter.get_normal_response(serializer.data)
        return Response(response_data)
