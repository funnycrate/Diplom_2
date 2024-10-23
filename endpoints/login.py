import requests
from data import BASE_URL

class LoginUser:
    def __init__(self):
        self.url = f"{BASE_URL}/auth/login"

    def login(self, email, password):
        """Метод для авторизации пользователя"""
        data = {
            "email": email,
            "password": password
        }
        response = requests.post(self.url, json=data)
        return response
