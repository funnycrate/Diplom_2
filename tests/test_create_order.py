import allure
import pytest
from endpoints.order import CreateOrder

@allure.feature('Управление заказами')
@allure.story('Создание заказов')
class TestOrderCreation:

    @allure.step("Создание заказа с авторизацией")
    def test_create_order_with_auth(self, create_user, get_user_token, get_ingredients):
        """Тест на создание заказа с авторизацией"""
        token = get_user_token(create_user["email"], create_user["password"])
        create_order = CreateOrder()

        order_data = {"ingredients": get_ingredients[:2]}
        response = create_order.create_with_auth(token, order_data)

        assert response.status_code == 200, f"Ожидался код ответа 200, но получен {response.status_code}, тело ответа: {response.text}"

    @allure.step("Создание заказа без авторизации")
    @pytest.mark.xfail(reason="Ожидается ошибка, но API возвращает 200")
    def test_create_order_without_auth(self, get_ingredients):
        """Тест на создание заказа без авторизации"""
        create_order = CreateOrder()

        order_data = {"ingredients": get_ingredients[:2]}
        response = create_order.create_without_auth(order_data)

        assert response.status_code == 401, f"Ожидался код ответа 401, но получен {response.status_code}, тело ответа: {response.text}"

    @allure.step("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, create_user, get_user_token):
        """Тест на создание заказа без ингредиентов"""
        token = get_user_token(create_user["email"], create_user["password"])
        create_order = CreateOrder()

        order_data = {"ingredients": []}
        response = create_order.create_with_auth(token, order_data)

        assert response.status_code == 400, f"Ожидался код ответа 400, но получен {response.status_code}, тело ответа: {response.text}"

    @allure.step("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingredient_hash(self, create_user, get_user_token):
        """Тест на создание заказа с неверным хешем ингредиентов"""
        token = get_user_token(create_user["email"], create_user["password"])
        create_order = CreateOrder()

        order_data = {"ingredients": ["invalid_hash"]}
        response = create_order.create_with_auth(token, order_data)

        assert response.status_code == 400, f"Ожидался код ответа 400, но получен {response.status_code}, тело ответа: {response.text}"