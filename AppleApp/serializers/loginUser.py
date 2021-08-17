from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from AppleApp.models import LoginUser
from AppleApp.util.util import name_validator, phone_number_validator, login_username_validator, password_validator


class LoginUserSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    name = serializers.CharField(
        allow_null=False,
        allow_blank=False,
        trim_whitespace=True,
        validators=[
            name_validator,
        ])
    phone_number = serializers.CharField(
        allow_null=False,
        allow_blank=False,
        trim_whitespace=True,
        validators=[
            phone_number_validator,
            UniqueValidator(
                queryset=LoginUser.custom_objects.all(),
                message="该电话已被注册")
        ])
    login_name = serializers.CharField(
        allow_null=False,
        allow_blank=False,
        trim_whitespace=True,
        validators=[
            login_username_validator,
            UniqueValidator(
                queryset=LoginUser.custom_objects.all(),
                message="该登陆用户名已被注册")
        ]
    )
    address = serializers.CharField(
        allow_blank=False,
        allow_null=False,
        trim_whitespace=True,
    )
    login_password = serializers.CharField(
        allow_null=False,
        allow_blank=False,
        trim_whitespace=True,
        validators=[
            password_validator,
        ]
    )
