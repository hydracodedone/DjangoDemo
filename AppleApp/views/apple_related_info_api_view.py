from drf_yasg2.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from AppleApp.model_action.apple_feature_action_set import AppleFeatureModelAction
from AppleApp.serializers.apple_feature_serializer import AppleFeatureSerializer
from FirstProject.util.customized_authentication_permission.custom_authentication import JWTAutentication, \
    custom_authentication_decorator
from FirstProject.util.customized_authentication_permission.custom_permission import CustomTestPermission, \
    custom_permission_decorator
from FirstProject.util.customized_response.global_response import ResponseFomatter


class AppleFeatureApi(APIView):
    authentication_classes = [JWTAutentication]
    permission_classes = [CustomTestPermission]

    @staticmethod
    @swagger_auto_schema(
        security=[],
        operation_description="查询苹果特征信息",
    )
    def get(request):
        data = AppleFeatureModelAction.query_all_apple_feature_info()
        serializer = AppleFeatureSerializer(many=False)
        serializer.instance = data
        response_data = ResponseFomatter.get_normal_response(serializer.data)
        return Response(response_data)
