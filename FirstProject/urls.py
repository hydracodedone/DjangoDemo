# encoding:UTF-8


from django.contrib import admin
from django.urls import path

from AppleApp.views.loginUser import LoginUserApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login_user/", LoginUserApi.as_view(), )
]
