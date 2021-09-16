# encoding:UTF-8


from django.contrib import admin
from django.urls import path
from rest_framework.documentation import include_docs_urls

from AppleApp.views.administrative_division_api_view import AdministrativeDivisionAPIView
from AppleApp.views.apple_api_view import AppleInfoManagerAPIView
from AppleApp.views.apple_feature_api_view import AppleFeatureApi
from AppleApp.views.login_user_api_view import LoginUserApi, TokenGenerageAPIView, TokenRefreshAPIView
from AppleApp.views.owner_type_api_view import OwnerTypeApi
from AppleApp.views.storage_type_api_view import StoragePoolTypeAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("docs/", include_docs_urls(title="API DOC")),

    path("user_info_management/", LoginUserApi.as_view()),
    path("refresh_token/", TokenRefreshAPIView.as_view()),
    path("login/", TokenGenerageAPIView.as_view()),

    path("owner_type/", OwnerTypeApi.as_view()),
    path("storage_pool_type/", StoragePoolTypeAPIView.as_view()),
    path("administrative_division/", AdministrativeDivisionAPIView.as_view()),
    path("apple_feature/", AppleFeatureApi.as_view()),
    path("apple_management/", AppleInfoManagerAPIView.as_view()),
]
