from users.api_user import ApiClient
from data import EndPointData, ConstantData
import allure


class TestGetUserOrders:

    path = EndPointData.PATH_ORDER
    path_login = EndPointData.PATH_USER_LOGIN

    @allure.title("Получение данных заказа.")
    @allure.description("Авторизованному пользователю вернется список заказов.")
    def test_get_authorize_user_true(self):
        api = ApiClient()
        response_login = api.post(self.path_login, ConstantData.BASE_USER)
        auth = response_login.json()['accessToken']
        response_get_order = api.get(self.path, auth)
        assert response_get_order.status_code == 200
        assert response_get_order.json()["success"] == True

    @allure.title("Получение данных заказа.")
    @allure.description("Неавторизованному пользователю список заказов недоступен.")
    def test_get_not_authorize_user_true(self):
        api = ApiClient()
        response_get_order = api.get(self.path)
        assert response_get_order.status_code == 401
        assert response_get_order.json()["message"] == "You should be authorised"
