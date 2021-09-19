from rest_framework.views import APIView

from FirstProject.util.customized_authentication_permission.custom_authentication import JWTAutentication
from FirstProject.util.customized_authentication_permission.custom_permission import CustomTestPermission


class StorageAPIView(APIView):
    authentication_classes = [JWTAutentication]
    permission_classes = [CustomTestPermission]

    @staticmethod
    def post(request):
        pass



