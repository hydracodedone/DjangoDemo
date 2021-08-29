from rest_framework.response import Response
from rest_framework.views import APIView

from AppleApp.model_action.apple_feature_action_set import AppleFeatureModelAction
from AppleApp.serializers.apple_feature_serializer import AppleFeatureSerializer
from FirstProject.util.customized_response.global_response import ResponseFomatter


class AppleFeatureApi(APIView):
    @staticmethod
    def get(request):
        data = AppleFeatureModelAction.query_all_apple_feature_info()
        serializer = AppleFeatureSerializer(many=False)
        serializer.instance = data
        response_data = ResponseFomatter.get_normal_response(serializer.data)
        return Response(response_data)
