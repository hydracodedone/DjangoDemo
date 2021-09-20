import json

from django.test import Client
from django.test import TestCase


class LoginUserTestCase(TestCase):
    def setUp(self):
        self.request_data = {
            "name": "王小二",
            "phone_number": "15719630526",
            "login_name": "Hydra",
            "login_password": "123456",
            "address": "甘肃省平凉市泾川县"
        }

    def test_user_register(self):
        client = Client()
        url = "http://localhost:8000/management/user/"
        response = client.post(path=url, data=self.request_data)
        print(response.json())

    def tearDown(self):
        pass
