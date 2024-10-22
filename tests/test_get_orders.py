import allure
import pytest
from endpoints.order import *

@allure.feature('Управление заказами')
@allure.story('Получение заказов')
class TestGetOrders:

    @allure.step("Получение заказов авторизованного пользователя")
    def test_get_orders_authorized_user(self, create_user, get_user_token):
        """Тест на получение заказов авторизованным пользователем"""
        token = get_user_token(create_user["email"], create_user["password"])

        # Создаем заказ, чтобы был хотя бы один заказ
        create_order = CreateOrder()
        ingredients_response = create_order.get_ingredients()
        assert ingredients_response.status_code == 200, "Не удалось получить список ингредиентов"
        ingredients = [ingredient["_id"] for ingredient in ingredients_response.json()["data"]]

        order_data = {
            "ingredients": ingredients[:2]  # Используем два ингредиента для заказа
        }
        create_order.create_with_auth(token, order_data)

        # Получаем заказы авторизованного пользователя
        get_orders = GetOrders()
        response = get_orders.get_orders_with_auth(token)

        # Проверка успешного получения заказов
        assert response.status_code == 200, f"Ожидался код ответа 200, но получен {response.status_code}"
        assert len(response.json()["orders"]) > 0, "Ожидался хотя бы один заказ у пользователя"

    @allure.step("Получение заказов неавторизованным пользователем")
    def test_get_orders_unauthorized_user(self):
        """Тест на получение заказов неавторизованным пользователем"""

        # Получение заказов без авторизации
        get_orders = GetOrders()
        response = get_orders.get_orders_without_auth()

        # Проверка, что запрос без авторизации вернет ошибку
        assert response.status_code == 401, f"Ожидался код ответа 401, но получен {response.status_code}"
