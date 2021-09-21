from drf_yasg2.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from AppleApp.model_action.personal_storage_pool_management import StoragePoolModelAction
from AppleApp.serializers.personal_storage_pool_serializer import StoragePoolCreateSerializer, \
    StoragePoolUpdateSerializer
from FirstProject.util.customized_authentication_permission.custom_authentication import JWTAutentication
from FirstProject.util.customized_authentication_permission.custom_permission import CustomTestPermission
from FirstProject.util.customized_response.global_response import ResponseFomatter, ADD, MODIFY


class StoragePollManagerAPIView(APIView):
    authentication_classes = [JWTAutentication]
    permission_classes = [CustomTestPermission]

    @staticmethod
    @swagger_auto_schema(
        security=[],
        operation_description="创建存储库信息",
    )
    def post(request):
        user = request.user
        data = request.data
        serializer = StoragePoolCreateSerializer(many=False, data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            StoragePoolModelAction.create_new_storage_pool(user, **validated_data)
        else:
            response_data = ResponseFomatter.get_validated_error(serializer.errors)
            return Response(response_data)
        response_data = ResponseFomatter.get_normal_response(ADD)
        return Response(response_data)

    @staticmethod
    @swagger_auto_schema(
        security=[],
        operation_description="创建存储库信息",
    )
    def post(request):
        user = request.user
        data = request.data
        serializer = StoragePoolCreateSerializer(many=False, data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            StoragePoolModelAction.create_new_storage_pool(user, **validated_data)
        else:
            response_data = ResponseFomatter.get_validated_error(serializer.errors)
            return Response(response_data)
        response_data = ResponseFomatter.get_normal_response(ADD)
        return Response(response_data)

    @staticmethod
    @swagger_auto_schema(
        security=[],
        operation_description="修改存储库信息",
    )
    def put(request):
        user = request.user
        data = request.data
        serializer = StoragePoolUpdateSerializer(many=False, data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            StoragePoolModelAction.update_storage_pool(user, **validated_data)
        else:
            response_data = ResponseFomatter.get_validated_error(serializer.errors)
            return Response(response_data)
        response_data = ResponseFomatter.get_normal_response(MODIFY)
        return Response(response_data)
