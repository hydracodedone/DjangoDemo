from rest_framework.exceptions import NotAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from AppleApp.model_action.storge_type_action_set import StorageTypeModelAction
from AppleApp.serializers.storage_type_serializer import StorageTypeSerializer
from FirstProject.util.customized_response.global_response import ResponseFomatter


class StoragePoolTypeAPIView(APIView):
    @staticmethod
    def get(request):
        data = StorageTypeModelAction.get_all_data()
        serialzier = StorageTypeSerializer(many=True)
        serialzier.instance = data
        response_data = ResponseFomatter.get_normal_response(serialzier.data)
        return Response(response_data)
