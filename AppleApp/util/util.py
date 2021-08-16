import re
import uuid
from datetime import datetime

from django.utils.timezone import utc
from rest_framework.exceptions import ValidationError


def uuid_general():
    return uuid.uuid4().hex


def get_now_time():
    return datetime.utcnow().replace(tzinfo=utc)


def name_validator(data):
    mode = r"^[\u4E00-\u9FA5]{2,4}$"
    pattern = re.compile(mode)
    result = pattern.match(data)
    if result is None:
        raise ValidationError("name is illegal")
    else:
        return data


def phone_number_validator(data):
    mode = r"^1[3|4|5|7|8|9]\d{9}$"
    pattern = re.compile(mode)
    result = pattern.match(data)
    if result is None:
        raise ValidationError("phone_number is illegal")



def login_username_validator(data):
    mode = r"^[a-zA-Z0-9_-]{4,16}$"
    pattern = re.compile(mode)
    result = pattern.match(data)
    if result is None:
        raise ValidationError("login_name is illegal")
    else:
        return data


def password_validator(data):
    mode = r"^.*(?=.{6,})(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*? ]).*$"
    pattern = re.compile(mode)
    result = pattern.match(data)
    if result is None:
        raise ValidationError("password is illegal")
    else:
        return data
