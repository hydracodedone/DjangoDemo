import datetime

import requests


def query_user_related_info():
    query_owner_type_response = requests.get("http://localhost:8000/common/user_info_related/")
    return query_owner_type_response.json()


def create_new_user(name_data, phone_number_data, login_name_data):
    data = {
        "name": name_data,
        "phone_number": phone_number_data,
        "login_name": login_name_data,
        "login_password": "123456",
        "address": "甘肃省平凉市泾川县",
        "owner_type_uid": query_user_related_info().get("data").get("owner_type")[0].get("owner_type_uid")
    }
    create_user_response = requests.post("http://localhost:8000/management/user/", json=data)
    print(create_user_response.json())


def update_user(token_data):
    data = {
        "token": token_data, "login_password": "1234567",
    }
    update_user_response = requests.put("http://localhost:8000/management/user/", json=data)
    print(update_user_response.json())


def refresh_token(token_data):
    refresh_data = {
        "token": token_data
    }
    generate_token_response = requests.put("http://localhost:8000/token/", json=refresh_data)
    print(generate_token_response.json())
    return generate_token_response.json().get("data").get("token")


def first_generate_token(login_name_data):
    generate_data = {
        "login_name": login_name_data,
        "login_password": "123456"
    }
    generate_token_response = requests.post("http://localhost:8000/token/", json=generate_data)
    print(generate_token_response.json())
    token_data = generate_token_response.json().get("data").get("token")
    return token_data


def generate_token():
    generate_data = {
        "login_name": "Hydra",
        "login_password": "1234567"
    }
    generate_token_response = requests.post("http://localhost:8000/token/", json=generate_data)
    print(generate_token_response.json())
    token_data = generate_token_response.json().get("data").get("token")
    return token_data


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
    return apple_related_info_response.json()


def get_storage_info_related_info():
    data = {
        "token": generate_token()
    }
    apple_related_info_response = requests.get("http://localhost:8000/common/storage_info_related/", params=data)
    print(apple_related_info_response.json())


def create_new_batch_apple_info():
    related_info = get_apple_related_info()

    data = {
        "token": generate_token(),
        "type": related_info.get("data").get("apple_type")[0].get("apple_type_uid"),
        "level": related_info.get("data").get("apple_level")[0].get("apple_level_uid"),
        "maturity": related_info.get("data").get("apple_maturity")[0].get("apple_maturity_uid"),
        "pesticide_residue": related_info.get("data").get("apple_pesticide_residue")[0].get(
            "apple_pesticde_residue_uid"),
        "packing_type": related_info.get("data").get("apple_packing_type")[0].get("apple_packing_type_uid"),
        "batch_name": "my batch",
        "sum_remaining": "1000",
        "price": "1.2",
        "product_time": datetime.datetime.date(datetime.datetime.now()).strftime("%Y-%m-%d"),
        "is_available": True,
    }
    apple_create_response = requests.post("http://localhost:8000/management/apple/", json=data)
    print(apple_create_response.json())


if __name__ == '__main__':
    name = "王译"
    phone_number = "17302841531"
    login_name = "hydra5"
    create_new_user(name, phone_number, login_name)
    token = first_generate_token(login_name)
    update_user(token)
    create_new_batch_apple_info()
