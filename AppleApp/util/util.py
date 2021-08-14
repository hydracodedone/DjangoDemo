import uuid
from datetime import datetime

from django.utils.timezone import utc


def uuid_general():
    return uuid.uuid4().hex


def get_now_time():
    return datetime.utcnow().replace(tzinfo=utc)
