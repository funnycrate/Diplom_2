from endpoints.update import *
import requests
import allure
from data import *

@allure.feature('Обновление данных пользователя')
class TestUpdateUser:

    @allure.step("Изменение email пользователя с авторизацией")
    def test_update_email_with_auth(self, create_user, get_user_token, unique_email):
        token = get_user_token(create_user["email"], create_user["password"])
        update_user = UpdateUser()
        updated_data = {"email": unique_email}
        response = update_user.update_with_auth(token, updated_data)

        assert response.status_code == 200, f"Ожидался код ответа 200, но получен {response.status_code}, текст ответа: {response.text}"

        create_user["new_email"] = updated_data["email"]

    @allure.step("Изменение email пользователя без авторизации")
    def test_update_email_without_auth(self, unique_email):
        update_user = UpdateUser()
        updated_data = {"email": unique_email}
        response = update_user.update_without_auth(updated_data)

        assert response.status_code == 401, f"Ожидался код ответа 401, но получен {response.status_code}, текст ответа: {response.text}"

    @allure.step("Изменение имени пользователя с авторизацией")
    def test_update_name_with_auth(self, create_user, get_user_token):
        token = get_user_token(create_user["email"], create_user["password"])
        update_user = UpdateUser()
        updated_data = {"name": "UpdatedName"}
        response = update_user.update_with_auth(token, updated_data)

        assert response.status_code == 200, f"Ожидался код ответа 200, но получен {response.status_code}, текст ответа: {response.text}"

    @allure.step("Изменение имени пользователя без авторизации")
    def test_update_name_without_auth(self):
        update_user = UpdateUser()
        updated_data = {"name": "UnauthorizedUpdate"}
        response = update_user.update_without_auth(updated_data)

        assert response.status_code == 401, f"Ожидался код ответа 401, но получен {response.status_code}, текст ответа: {response.text}"

    @allure.step("Изменение пароля пользователя с авторизацией")
    def test_update_password_with_auth(self, create_user, get_user_token):
        token = get_user_token(create_user["email"], create_user["password"])
        update_user = UpdateUser()
        updated_data = {"password": "NewPassword123"}
        response = update_user.update_with_auth(token, updated_data)

        assert response.status_code == 200, f"Ожидался код ответа 200, но получен {response.status_code}, текст ответа: {response.text}"
        new_token = get_user_token(create_user["email"], updated_data["password"])

        assert new_token is not None, "Не удалось получить токен с новым паролем"
        create_user["password"] = updated_data["password"]
