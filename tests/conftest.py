import requests
import random
import string
import pytest


# если регистрация не удалась, возвращает пустой список
@pytest.fixture(scope="session")
def register_new_user_and_return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    name = generate_random_string(10)
    password = generate_random_string(10)
    email = f'{name}@mail_test.ru'

    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(' https://stellarburgers.nomoreparties.site/api/auth/register', data=payload)

    if response.status_code == 200:
        login_pass.append(name)
        login_pass.append(password)
        login_pass.append(email)

    # возвращаем список
    return login_pass

