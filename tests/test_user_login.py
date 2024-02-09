import pytest
from users.api_user import ApiClient
from data import ConstantData, EndPointData, TestData
import allure


class TestUserLogin:

    path = EndPointData.PATH_USER_LOGIN

    @allure.title("Успешная авторизация пользователя с валидными данными.")
    @allure.description("Страница авторизации пользователя.")
    def test_user_login_true(self):
        api = ApiClient()
        response = api.post(self.path, ConstantData.BASE_USER)
        assert response.status_code == 200
        assert response.json()["success"] == True

    @allure.title("При авторизации пользователя с неверными данными выходит ошибка.")
    @allure.description("Логин с неверными данными.")
    @pytest.mark.parametrize('payload', TestData.wrong_data)
    def test_full_fields_false(self, payload):
        api = ApiClient()
        response = api.post(self.path, payload)
        assert response.status_code == 401
        assert response.json()["message"] == "email or password are incorrect"
