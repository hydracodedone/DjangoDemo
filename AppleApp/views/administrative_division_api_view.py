from rest_framework.response import Response
from rest_framework.views import APIView

from AppleApp.model_action.adminstation_area_action_set import AdminstrativeDivisionAction
from AppleApp.serializers.administrative_division_serializer import AdministrativeDivisionSerializer


class AdministrativeDivisionAPIView(APIView):

    @staticmethod
    def get(request):
        data = AdminstrativeDivisionAction.query_all_administrative_data()
        serializer = AdministrativeDivisionSerializer(many=True)
        serializer.instance = data
        return Response(serializer.data)
