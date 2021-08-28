from rest_framework.response import Response
from rest_framework.views import APIView

from AppleApp.model_action.storge_type_action_set import StorageTypeModelAction
from AppleApp.serializers.storage_type_serializer import StorageTypeSerializer


class StoragePoolTypeAPIView(APIView):
    @staticmethod
    def get(request):
        data = StorageTypeModelAction.get_all_data()
        serialzier = StorageTypeSerializer(many=True)
        serialzier.instance = data
        return Response(serialzier.data)
