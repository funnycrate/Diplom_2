import requests
import allure
from data import BASE_URL

class RegisterUser:
    def __init__(self):
        self.url = f"{BASE_URL}/auth/register"

    @allure.step("Регистрация нового пользователя")
    def create_user(self, user_data):
        """Метод для регистрации пользователя"""
        response = requests.post(self.url, json=user_data)
        return response
