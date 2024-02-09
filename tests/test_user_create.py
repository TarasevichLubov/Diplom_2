import allure
from users.api_user import ApiClient
from data import EndPointData


class TestUsers:

    path = EndPointData.PATH_CREATE_USERS

    @allure.title("Успешная регистрация нового пользователя с валидными данными.")
    @allure.description("Пользователь создан.")
    def test_user_create_true(self, register_new_user_and_return_login_password):
        assert len(register_new_user_and_return_login_password) > 0

    @allure.title("Регистрация нового пользователя с ранее созданными параметрами невозможна.")
    @allure.description("Нельзя создать двух одинаковых пользователей.")
    def test_double_user_create(self, register_new_user_and_return_login_password):
        api = ApiClient()
        payload_data = {"name": register_new_user_and_return_login_password[0],
                        "password": register_new_user_and_return_login_password[1],
                        "email": register_new_user_and_return_login_password[2]}
        response = api.post(self.path, payload_data)
        assert response.status_code == 403
        assert response.json()['message'] == 'User already exists'

    @allure.title("Регистрация нового пользователя с пустыми параметрами.")
    @allure.description("Нельзя создать пользователя с пустыми параметрами.")
    def test_null_data_user_create_false(self, register_new_user_and_return_login_password):
        api = ApiClient()
        payload_data = {"name": "",
                        "password": "",
                        "email": ""}
        response = api.post(self.path, payload_data)
        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"
