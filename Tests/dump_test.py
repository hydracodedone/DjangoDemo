import requests


def query_user_related_info():
    """
    {
      "msg": "handle success",
      "err": "",
      "data": [
        {
          "owner_type_uid": "5ebe7824-def1-4fea-be9a-1a5863cc8c4e",
          "owner_type_name": "果农"
        },
        {
          "owner_type_uid": "6cbd4471-e2d3-49fd-a87b-1b42558feaf4",
          "owner_type_name": "顾客"
        },
        {
          "owner_type_uid": "a1498f49-836f-41c0-97ba-87239afb0316",
          "owner_type_name": "供应商"
        }
      ]
    }
    """
    query_owner_type = requests.get("http://localhost:8000/common/user_info_related/")
    print(query_owner_type.text)


def create_new_user():
    data = {
        "name": "王小二",
        "phone_number": "15719630526",
        "login_name": "Hydra",
        "login_password": "123456",
        "address": "甘肃省平凉市泾川县",
        "owner_type_uid": "a1498f49-836f-41c0-97ba-87239afb0316"
    }
    create_user_response = requests.post("http://localhost:8000/management/user/", json=data)
    print(create_user_response.json())


def update_user():
    data = {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNzAyYmMwM2UtZGU4Ny00YWQwLWI4NzItMGRkMDYxMDliMGQ2IiwidXNlcl9uYW1lIjoiSHlkcmEiLCJleHAiOjE2MzIxNDk2NDksIm9yaWdfaWF0IjoxNjMyMTQ3ODQ5fQ.frL2X0CdLBl2nYLMQdiKLwWbYL5zTwDFNfaWLQ1jl-o",
        "login_password": "1234567",
    }
    update_user_response = requests.put("http://localhost:8000/management/user/", json=data)
    print(update_user_response.json())


def refresh_token(token):
    refresh_data = {
        "token": token
    }
    generate_token_response = requests.put("http://localhost:8000/token/", json=refresh_data)
    print(generate_token_response.json())
    return generate_token_response.json().get("data").get("token")


def generate_token():
    generate_data = {
        "login_name": "Hydra",
        "login_password": "1234567"
    }
    generate_token_response = requests.post("http://localhost:8000/token/", json=generate_data)
    print(generate_token_response.json())
    token = generate_token_response.json().get("data").get("token")
    return token


def get_administrative_division_info():
    data = {
        "token": generate_token()
    }
    apple_related_info_response = requests.get("http://localhost:8000/common/administrative_division/", params=data)
    print(apple_related_info_response.json())


def get_apple_related_info():
    data = {
        "token": generate_token()
    }
    apple_related_info_response = requests.get("http://localhost:8000/common/apple_info_related/", params=data)
    print(apple_related_info_response.json())


def get_storage_info_related_info():
    data = {
        "token": generate_token()
    }
    apple_related_info_response = requests.get("http://localhost:8000/common/storage_info_related/", params=data)
    print(apple_related_info_response.json())


if __name__ == '__main__':
    get_administrative_division_info()
    get_apple_related_info()
    get_storage_info_related_info()
