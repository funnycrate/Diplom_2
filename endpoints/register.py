import requests
from data import BASE_URL

class RegisterUser:
    def __init__(self):
        self.url = f"{BASE_URL}/auth/register"

    def create_user(self, user_data):
        """Метод для регистрации пользователя"""
        response = requests.post(self.url, json=user_data)
        return response
