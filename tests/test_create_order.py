from users.api_user import ApiClient
from data import TestData, EndPointData
from const_data import ConstantData
import allure


class TestOrders:
    path = EndPointData.PATH_ORDER
    path_login = EndPointData.PATH_USER_LOGIN

    @allure.title("Успешное создание заказа с валидными данными с ингредиентами.")
    @allure.description("С авторизацией заказ создается.")
    def test_create_order_with_authorization_true(self):
        api = ApiClient()
        response_login = api.post(self.path_login, ConstantData.BASE_USER)
        auth = response_login.json()['accessToken']
        payload = {"ingredients": TestData.order_with_ingredients,
                   'Authorization': auth}
        response = api.post(self.path, payload)
        assert response.json()["success"] == True

    @allure.title("Успешное создание заказа.")
    @allure.description("Неавторизованный пользователь может создать заказ.")
    def test_create_order_without_authorization_true(self):
        api = ApiClient()
        payload = {"ingredients": TestData.order_with_ingredients}
        response = api.post(self.path, payload)
        assert response.json()["success"] == True

    @allure.title("Ошибка при создании заказа")
    @allure.description("Без ингредиентов нельзя создать заказ.")
    def test_create_order_without_ingredients_false(self):
        api = ApiClient()
        payload = {"ingredients": None}
        response = api.post(self.path, payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Ошибка при создании заказа")
    @allure.description("С неверным хешем нельзя создать заказ.")
    def test_create_order_with_incorrect_ingredients_false(self):
        api = ApiClient()
        payload = {"ingredients": TestData.order_with_wrong_hash_ingredients}
        response = api.post(self.path, payload)
        assert response.status_code == 500
