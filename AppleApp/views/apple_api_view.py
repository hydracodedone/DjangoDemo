from rest_framework.response import Response
from rest_framework.views import APIView

from AppleApp.model_action.apple_action_set import AppleModelAction
from AppleApp.serializers.apple_info_serializer import AppleInstanceAppleInfoWriteSerializer
from FirstProject.util.customized_authentication_permission.custom_authentication import JWTAutentication
from FirstProject.util.customized_authentication_permission.custom_permission import CustomTestPermission
from FirstProject.util.customized_response.global_response import ResponseFomatter, ADD


class AppleInfoManagerAPIView(APIView):
    authentication_classes = [JWTAutentication]
    permission_classes = [CustomTestPermission]

    @staticmethod
    def post(request):
        owner_id = request.user.owner.uid
        data = request.data
        serializer = AppleInstanceAppleInfoWriteSerializer(many=False, data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            validated_data.update(owner_id=owner_id)
            AppleModelAction.create_new_batch_apple(**validated_data)
        else:
            response_data = ResponseFomatter.get_validated_error(serializer.errors)
            return Response(response_data)
        response_data = ResponseFomatter.get_normal_response(ADD)
        return Response(response_data)

    def put(self, request):
        pass

    def delete(self):
        pass

    def get(self):
        pass
