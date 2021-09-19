from rest_framework.response import Response
from rest_framework.views import APIView

from AppleApp.model_action.apple_action_set import AppleModelAction
from AppleApp.serializers.apple_info_serializer import AppleInstanceAppleInfoCreateSerializer, \
    AppleInstanceAppleInfoUpdateSerializer, AppleInstanceAppleInfoDeleteSerializer
from FirstProject.util.customized_authentication_permission.custom_authentication import JWTAutentication
from FirstProject.util.customized_authentication_permission.custom_permission import CustomTestPermission
from FirstProject.util.customized_response.global_response import ResponseFomatter, ADD, MODIFY


class AppleInfoManagerAPIView(APIView):
    authentication_classes = [JWTAutentication]
    permission_classes = [CustomTestPermission]

    @staticmethod
    def post(request):
        owner_id = request.user.owner.uid
        data = request.data
        serializer = AppleInstanceAppleInfoCreateSerializer(many=False, data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            validated_data.update(owner_id=owner_id)
            AppleModelAction.create_new_apple_storage_info(**validated_data)
        else:
            response_data = ResponseFomatter.get_validated_error(serializer.errors)
            return Response(response_data)
        response_data = ResponseFomatter.get_normal_response(ADD)
        return Response(response_data)

    @staticmethod
    def put(request):
        user_uid = request.user.uid
        data = request.data
        serializer = AppleInstanceAppleInfoUpdateSerializer(many=False, data=data, context={"user_uid": user_uid})
        if serializer.is_valid():
            validated_data = serializer.validated_data
            AppleModelAction.update_new_apple_storage_info(**validated_data)
        else:
            response_data = ResponseFomatter.get_validated_error(serializer.errors)
            return Response(response_data)
        response_data = ResponseFomatter.get_normal_response(MODIFY)
        return Response(response_data)

    @staticmethod
    def delete(request):
        user_uid = request.user.uid
        data = request.data
        serializer = AppleInstanceAppleInfoDeleteSerializer(many=False, data=data, context={"user_uid": user_uid})
        if serializer.is_valid():
            validated_data = serializer.validated_data
            AppleModelAction.delete_apple_storage_info(**validated_data)
        else:
            response_data = ResponseFomatter.get_validated_error(serializer.errors)
            return Response(response_data)
        response_data = ResponseFomatter.get_normal_response(MODIFY)
        return Response(response_data)
