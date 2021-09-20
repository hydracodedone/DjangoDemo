# encoding:UTF-8
from django.contrib import admin
from django.urls import path
from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view

from AppleApp.views.administrative_division_api_view import AdministrativeDivisionAPIView
from AppleApp.views.apple_api_view import AppleInfoManagerAPIView
from AppleApp.views.apple_related_info_api_view import AppleFeatureApi
from AppleApp.views.storage_related_info_api_view import StorageInfoAPIView
from AppleApp.views.token_api_view import TokenManagementAPIView
from AppleApp.views.user_api_view import LoginUserApi
from AppleApp.views.user_related_info_api_view import UserRelatedInfoAPIView

schema_view = get_schema_view(
    openapi.Info(
        title="Backends API",
        default_version="v1",
        description=""
    ),
    public=True,
    permission_classes=(),
)
urlpatterns = [
    path('admin/', admin.site.urls),
]
swagger_doc_url = [
    path("docs/swagger_doc/", schema_view.with_ui("swagger", cache_timeout=0)),
    path("docs/swagger_redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
]

related_info_url = [
    path("common/administrative_division/", AdministrativeDivisionAPIView.as_view()),
    path("common/user_info_related/", UserRelatedInfoAPIView.as_view()),
    path("common/apple_info_related/", AppleFeatureApi.as_view()),
    path("common/storage_info_related/", StorageInfoAPIView.as_view()),
]

token_management_url = [
    path("token/", TokenManagementAPIView.as_view()),
]
management_url = [
    path("management/user/", LoginUserApi.as_view()),
    path("management/apple/", AppleInfoManagerAPIView.as_view())
]
storage_url = [

]
urlpatterns.extend(related_info_url)
urlpatterns.extend(swagger_doc_url)
urlpatterns.extend(token_management_url)
urlpatterns.extend(management_url)
