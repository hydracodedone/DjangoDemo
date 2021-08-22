from rest_framework.views import APIView

from AppleApp.modelAction.onwer_type_action_set import OwnerTypeModelAction
from AppleApp.serializers.onwer_type_serializer import OwnerTypeSerializer
from AppleApp.util.pagination.custom_pagination import CustomPagination


class OwnerTypeApi(APIView):
    @staticmethod
    def get(request):
        data = OwnerTypeModelAction.get_all_data()
        pagenition = CustomPagination()
        paged_data = pagenition.paginate_queryset(queryset=data, request=request, view=OwnerTypeApi.get)
        serializer = OwnerTypeSerializer(many=True)
        serializer.instance = paged_data
        serialized_data = serializer.data
        return pagenition.get_paginated_response(serialized_data)
