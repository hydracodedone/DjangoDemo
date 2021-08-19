# encoding:UTF-8


from django.contrib import admin
from django.urls import path
from rest_framework.documentation import include_docs_urls

from AppleApp.views.loginUser import LoginUserApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login_user/", LoginUserApi.as_view()),
    path("docs/", include_docs_urls(title="API DOC"))
]
