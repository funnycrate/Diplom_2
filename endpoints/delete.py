import requests
import allure
from data import BASE_URL

class DeleteUser:
    def __init__(self):
        self.url = f"{BASE_URL}/auth/user"

    @allure.step("Удаление пользователя")
    def delete(self, token):
        """Метод для удаления пользователя"""
        headers = {'Authorization': token}
        response = requests.delete(self.url, headers=headers)
        return response
