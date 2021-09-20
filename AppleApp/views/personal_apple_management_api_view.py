from drf_yasg2.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from AppleApp.model_action.personal_apple_management import AppleModelAction
from AppleApp.serializers.personal_apple_info_serializer import AppleInstanceCreateSerializer, \
    AppleInstanceAppleInfoUpdateSerializer, AppleInstanceAppleInfoDeleteSerializer
from FirstProject.util.customized_authentication_permission.custom_authentication import JWTAutentication
from FirstProject.util.customized_authentication_permission.custom_permission import CustomTestPermission
from FirstProject.util.customized_response.global_response import ResponseFomatter, ADD, MODIFY


class AppleInfoManagerAPIView(APIView):
    authentication_classes = [JWTAutentication]
    permission_classes = [CustomTestPermission]

    @staticmethod
    @swagger_auto_schema(
        security=[],
        operation_description="创建个人苹果信息",
    )
    def post(request):
        owner_id = request.user.owner.uid
        data = request.data
        serializer = AppleInstanceCreateSerializer(many=False, data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            validated_data.update(owner_id=owner_id)
            AppleModelAction.create_new_batch_apple(**validated_data)
        else:
            response_data = ResponseFomatter.get_validated_error(serializer.errors)
            return Response(response_data)
        response_data = ResponseFomatter.get_normal_response(ADD)
        return Response(response_data)

    @staticmethod
    @swagger_auto_schema(
        security=[],
        operation_description="修改个人苹果信息",
    )
    def put(request):
        user_uid = request.user.uid
        data = request.data
        serializer = AppleInstanceAppleInfoUpdateSerializer(many=False, data=data, context={"user_uid": user_uid})
        if serializer.is_valid():
            validated_data = serializer.validated_data
            AppleModelAction.update_apple_info(**validated_data)
        else:
            response_data = ResponseFomatter.get_validated_error(serializer.errors)
            return Response(response_data)
        response_data = ResponseFomatter.get_normal_response(MODIFY)
        return Response(response_data)

    @staticmethod
    @swagger_auto_schema(
        security=[],
        operation_description="删除个人苹果信息",
    )
    def delete(request):
        user_uid = request.user.uid
        data = request.data
        serializer = AppleInstanceAppleInfoDeleteSerializer(many=False, data=data, context={"user_uid": user_uid})
        if serializer.is_valid():
            validated_data = serializer.validated_data
            AppleModelAction.delete_apple_info(**validated_data)
        else:
            response_data = ResponseFomatter.get_validated_error(serializer.errors)
            return Response(response_data)
        response_data = ResponseFomatter.get_normal_response(MODIFY)
        return Response(response_data)

    @staticmethod
    @swagger_auto_schema(
        security=[],
        operation_description="查询个人苹果信息",
    )
    def get(request):
        owner_uid = request.user.owner.uid
        data = AppleModelAction.query_apple_info(owner_uid=owner_uid)
        serializer = AppleInstanceAppleInfoUpdateSerializer(many=True)
        serializer.instance = data
        response_data = ResponseFomatter.get_normal_response(serializer.data)
        return Response(response_data)
