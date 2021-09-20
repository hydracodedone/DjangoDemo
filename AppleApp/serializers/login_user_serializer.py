from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from AppleApp.models import LoginUser
from AppleApp.serializers.login_user_related_info_serializer import OwnerTypeUidForLoginUserSeriazlier
from FirstProject.util.constant.validate_error import PHONE_HAS_BEEN_REGISTERED, LOGIN_NAME_HAS_BEEN_REGISTERED
from FirstProject.util.validate_function.validate_function import name_validator, phone_number_validator, \
    login_username_validator, password_validator


class LoginUserOriginalSerializer(serializers.Serializer):
    name = serializers.CharField(
        allow_null=False,
        allow_blank=False,
        required=True,
        trim_whitespace=True,
        validators=[
            name_validator,
        ])
    phone_number = serializers.CharField(
        allow_null=False,
        allow_blank=False,
        required=True,
        trim_whitespace=True,
        validators=[
            phone_number_validator,
            UniqueValidator(
                queryset=LoginUser.custom_objects.only("phone_number"),
                message=PHONE_HAS_BEEN_REGISTERED)
        ])
    login_name = serializers.CharField(
        allow_null=False,
        allow_blank=False,
        required=True,
        trim_whitespace=True,
        validators=[
            login_username_validator,
            UniqueValidator(
                queryset=LoginUser.custom_objects.all(),
                message=LOGIN_NAME_HAS_BEEN_REGISTERED)
        ]
    )
    address = serializers.CharField(
        allow_blank=False,
        allow_null=False,
        required=True,
        trim_whitespace=True,
    )

    def update(self, instance, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    def create(self, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")


class LoginUserCreateSerializer(LoginUserOriginalSerializer, OwnerTypeUidForLoginUserSeriazlier,
                                serializers.Serializer):
    def update(self, instance, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    def create(self, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    login_password = serializers.CharField(
        required=True,
        allow_null=False,
        allow_blank=False,
        trim_whitespace=True,
        validators=[
            password_validator,
        ]
    )


class LoginUserUpdateSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    def create(self, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    name = serializers.CharField(
        allow_null=True,
        allow_blank=True,
        required=False,
        trim_whitespace=True,
        validators=[
            name_validator,
        ])
    phone_number = serializers.CharField(
        allow_null=True,
        allow_blank=True,
        required=False,
        trim_whitespace=True,
        validators=[
            phone_number_validator,
            UniqueValidator(
                queryset=LoginUser.custom_objects.all().only("phone_number"),
                message=PHONE_HAS_BEEN_REGISTERED)
        ])
    login_name = serializers.CharField(
        allow_null=True,
        allow_blank=True,
        required=False,
        trim_whitespace=True,
        validators=[
            login_username_validator,
            UniqueValidator(
                queryset=LoginUser.custom_objects.all().only("login_name"),
                message=LOGIN_NAME_HAS_BEEN_REGISTERED)
        ]
    )
    address = serializers.CharField(
        allow_blank=True,
        allow_null=True,
        required=False,
        trim_whitespace=True,
    )
    login_password = serializers.CharField(
        allow_null=True,
        allow_blank=True,
        required=False,
        trim_whitespace=True,
        validators=[
            password_validator,
        ]
    )


class LoginUserLoginSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    def create(self, validated_data):
        raise NotImplementedError("DO NOT NEED IMPLEMENTED")

    login_name = serializers.CharField(
        allow_null=False,
        allow_blank=False,
        required=True,
        trim_whitespace=True,
    )

    login_password = serializers.CharField(
        allow_null=False,
        allow_blank=False,
        required=True,
        trim_whitespace=True,
    )
