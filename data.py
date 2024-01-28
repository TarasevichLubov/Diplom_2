import random


class ConstantData:

    DEFAULT_HEADERS = {"accept": "application/json", "Content-Type": "application/json"}
    BASE_USER = {"name": 'IvanSmirnov', "password": 'IvanSmirnov12345', "email": 'IvanSmirnov@testmail.com'}


class TestData:

    wrong_data = [
        {"name": 'TestingUser_wrong', "password": '123456', "email": 'TestingUser_wrong@testmail.ru'}
    ]
    update_user_data = [
        {"name": "TestUserData"},
        {"password": "0000000"},
        {"email": "TestUserData@testmail.ru"},
    ]
    order_with_ingredients = ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa73"]
    order_with_wrong_hash_ingredients = ["61","75"]


class EndPointData:

    BASE_URL = "https://stellarburgers.nomoreparties.site/"
    PATH_CREATE_USERS = "api/auth/register"
    PATH_USER_LOGIN = "api/auth/login"
    PATH_USER_INFO = "api/auth/user"
    PATH_ORDER = "api/orders"
