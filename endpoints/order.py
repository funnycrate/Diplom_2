import requests
from data import BASE_URL

class CreateOrder:
    def __init__(self):
        self.create_order_url = f"{BASE_URL}/orders"
        self.ingredients_url = f"{BASE_URL}/ingredients"

    def create_with_auth(self, token, order_data):
        """Создание заказа с авторизацией"""
        headers = {"Authorization": token}
        response = requests.post(self.create_order_url, json=order_data, headers=headers)
        return response

    def create_without_auth(self, order_data):
        """Создание заказа без авторизации"""
        response = requests.post(self.create_order_url, json=order_data)
        return response

    def get_ingredients(self):
        """Получение доступных ингредиентов"""
        response = requests.get(self.ingredients_url)
        return response

class GetOrders:
    def __init__(self):
        self.endpoint = "/orders"

    def get_orders_with_auth(self, token):
        """Получение заказов авторизованного пользователя"""
        headers = {'authorization': token}
        response = requests.get(f"{BASE_URL}{self.endpoint}", headers=headers)
        return response

    def get_orders_without_auth(self):
        """Получение заказов неавторизованного пользователя"""
        response = requests.get(f"{BASE_URL}{self.endpoint}")
        return response

