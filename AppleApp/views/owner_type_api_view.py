from rest_framework.response import Response
from rest_framework.views import APIView

from AppleApp.model_action.onwer_type_action_set import OwnerTypeModelAction
from AppleApp.serializers.onwer_type_serializer import OwnerTypeSerializer
from FirstProject.util.customized_response.global_response import ResponseFomatter


class OwnerTypeApi(APIView):
    @staticmethod
    def get(request):
        data = OwnerTypeModelAction.get_all_data()
        serializer = OwnerTypeSerializer(many=True)
        serializer.instance = data
        response_data = ResponseFomatter.get_normal_response(serializer.data)
        return Response(response_data)
