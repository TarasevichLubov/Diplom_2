import pytest

from users.api_user import ApiClient
from data import EndPointData, TestData
import allure


class TestUserChange:

    path = EndPointData.PATH_USER_INFO
    path_login = EndPointData.PATH_USER_LOGIN
    token = None

    def setup_method(self):
        self.run_teardown = True

    @allure.title("Редактирование данных авторизованного пользователя.")
    @allure.description("Авторизованный пользователь может отредактировать данные своей учетной записи.")
    @pytest.mark.parametrize('update_data', TestData.update_user_data)
    def test_user_change_name_auth_true(self, register_new_user_and_return_login_password, update_data):
        api = ApiClient()
        payload_data = {"name": register_new_user_and_return_login_password[0],
                        "password": register_new_user_and_return_login_password[1],
                        "email": register_new_user_and_return_login_password[2]}
        response_login = api.post(self.path_login, payload_data)
        auth = response_login.json()['accessToken']
        self.token = auth
        response = api.patch(self.path, update_data, auth)
        assert response.json()["success"] == True

    @allure.title("Редактирование данных неавторизованного пользователя.")
    @allure.description("Неавторизованный пользователь не может отредактировать данные своей учетной записи.")
    @pytest.mark.parametrize('update_data', TestData.update_user_data)
    def test_user_change_name_auth_false(self, update_data):
        self.run_teardown = False
        api = ApiClient()
        response = api.patch(self.path, update_data)
        assert response.json()["success"] == False
        assert response.json()["message"] == "You should be authorised"

    def teardown_method(self):
        if self.run_teardown:
            api = ApiClient()
            api.delete(self.path_login, self.token)
