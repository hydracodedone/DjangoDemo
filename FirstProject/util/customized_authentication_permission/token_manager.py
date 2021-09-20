from calendar import timegm
from datetime import datetime, timedelta

import jwt
from django.apps import apps as django_apps
from django.core.exceptions import ImproperlyConfigured
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_jwt.settings import api_settings

from AppleApp.model_action.login_user_management import LoginModelAction
from FirstProject.util.constant.authentication_error import SIGNATURE_HAS_EXPIRED, SIGNATURE_DECODE_FAIL, \
    SIGNATURE_INVALID, SIGNATURE_FORGED


class UserLoginJWTAuthenticationExecption(AuthenticationFailed):
    pass


class UserLoginJWTAuthentication(object):
    @classmethod
    def get_user_model(cls):
        try:
            return django_apps.get_model(api_settings.AUTH_USER_MODEL, require_ready=False)
        except ValueError:
            raise ImproperlyConfigured("AUTH_USER_MODEL must be of the form 'app_label.model_name'")
        except LookupError:
            raise ImproperlyConfigured(
                "AUTH_USER_MODEL refers to model '%s' that has not been installed" % api_settings.AUTH_USER_MODEL
            )

    @classmethod
    def jwt_get_secret_key(cls, payload=None):
        if api_settings.JWT_GET_USER_SECRET_KEY:
            user_model = cls.get_user_model()
            user = user_model.objects.get(pk=payload.get(api_settings.AUTH_USER_UID))
            key = str(api_settings.JWT_GET_USER_SECRET_KEY(user))
            return key
        return api_settings.JWT_SECRET_KEY

    @classmethod
    def jwt_payload_handler(cls, user_data):
        user_id = getattr(user_data, "uid")
        user_name = getattr(user_data, "login_name")
        payload = {
            'user_id': user_id.__str__(),
            'user_name': user_name,
            'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
        }
        if api_settings.JWT_ALLOW_REFRESH:
            payload['orig_iat'] = timegm(
                datetime.utcnow().utctimetuple()
            )
        if api_settings.JWT_AUDIENCE is not None:
            payload['aud'] = api_settings.JWT_AUDIENCE
        if api_settings.JWT_ISSUER is not None:
            payload['iss'] = api_settings.JWT_ISSUER
        return payload

    @classmethod
    def jwt_get_user_id_from_payload_handler(cls, payload):
        return payload.get('user_id').__str__()

    @classmethod
    def jwt_get_user_name_from_payload_handler(cls, payload):
        return payload.get('user_name')

    @classmethod
    def jwt_encode_handler(cls, payload):
        key = api_settings.JWT_PRIVATE_KEY or cls.jwt_get_secret_key(payload)
        return jwt.encode(
            payload,
            key,
            api_settings.JWT_ALGORITHM
        ).decode('utf-8')

    @classmethod
    def jwt_decode_handler(cls, token):
        options = {
            'verify_exp': api_settings.JWT_VERIFY_EXPIRATION,
        }
        unverified_payload = jwt.decode(token, "", False, api_settings.JWT_ALGORITHM)
        secret_key = cls.jwt_get_secret_key(unverified_payload)
        return jwt.decode(
            token,
            api_settings.JWT_PUBLIC_KEY or secret_key,
            api_settings.JWT_VERIFY,
            options=options,
            leeway=api_settings.JWT_LEEWAY,
            audience=api_settings.JWT_AUDIENCE,
            issuer=api_settings.JWT_ISSUER,
            algorithms=[api_settings.JWT_ALGORITHM]
        )

    @classmethod
    def jwt_response_payload_handler(cls, token):
        return {
            'token': token
        }

    @classmethod
    def generate_token(cls, user_data):
        play_load = cls.jwt_payload_handler(user_data)
        token = cls.jwt_encode_handler(play_load)
        return cls.jwt_response_payload_handler(token)

    @classmethod
    def _check_payload(cls, token):
        try:
            payload = cls.jwt_decode_handler(token)
        except jwt.ExpiredSignature:
            msg = SIGNATURE_HAS_EXPIRED
            raise UserLoginJWTAuthenticationExecption(msg)
        except jwt.DecodeError:
            msg = SIGNATURE_DECODE_FAIL
            raise UserLoginJWTAuthenticationExecption(msg)
        return payload

    @classmethod
    def _check_user(cls, payload):
        user_name = cls.jwt_get_user_name_from_payload_handler(payload)
        user_uid = cls.jwt_get_user_id_from_payload_handler(payload)
        if not user_name or not user_uid:
            msg = SIGNATURE_INVALID
            raise UserLoginJWTAuthenticationExecption(msg)
        else:
            data = {
                "uid": user_uid,
                "login_name": user_name
            }
            user = LoginModelAction.query_user_by_uid_and_user_name(**data)
            if not user:
                msg = SIGNATURE_FORGED
                raise UserLoginJWTAuthenticationExecption(msg)
            else:
                return user

    @classmethod
    def refresh_token(cls, **validated_data):
        token = validated_data.get("token")
        payload = cls._check_payload(token=token)
        user = cls._check_user(payload=payload)
        orig_iat = payload.get('orig_iat')

        if orig_iat:
            refresh_limit = api_settings.JWT_REFRESH_EXPIRATION_DELTA
            if isinstance(refresh_limit, timedelta):
                refresh_limit = (refresh_limit.days * 24 * 3600 +
                                 refresh_limit.seconds)

            expiration_timestamp = orig_iat + int(refresh_limit)
            now_timestamp = timegm(datetime.utcnow().utctimetuple())

            if now_timestamp > expiration_timestamp:
                msg = SIGNATURE_HAS_EXPIRED
                raise UserLoginJWTAuthenticationExecption(msg)
        else:
            msg = SIGNATURE_FORGED
            raise UserLoginJWTAuthenticationExecption(msg)
        new_payload = cls.jwt_payload_handler(user)
        new_payload['orig_iat'] = orig_iat
        token = cls.jwt_encode_handler(new_payload)
        return cls.jwt_response_payload_handler(token)

    @classmethod
    def revify_token(cls, token):
        payload = cls._check_payload(token=token)
        user = cls._check_user(payload=payload)
        return user
