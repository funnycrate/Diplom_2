import requests
import allure
from data import BASE_URL

class UpdateUser:
    def __init__(self):
        self.url = f"{BASE_URL}/auth/user"

    @allure.step("Изменение данных пользователя с авторизацией")
    def update_with_auth(self, token, updated_data):
        """Изменение данных пользователя с авторизацией"""
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        response = requests.patch(self.url, headers=headers, json=updated_data)
        return response

    @allure.step("Попытка изменения данных без авторизации")
    def update_without_auth(self, updated_data):
        """Попытка изменения данных без авторизации"""
        response = requests.patch(self.url, json=updated_data)
        return response
