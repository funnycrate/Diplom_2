import allure
from endpoints.login import LoginUser

@allure.feature('Авторизация пользователя')
class TestLoginUser:

    @allure.step("Успешная авторизация пользователя")
    def test_login_existing_user(self, create_user):
        """Тест на успешную авторизацию"""
        user_data = create_user
        login_user = LoginUser()
        response = login_user.login(user_data["email"], user_data["password"])

        with allure.step("Проверка успешной авторизации"):
            assert response.status_code == 200, f"Ожидался код ответа 200, но получен {response.status_code}"
            assert "accessToken" in response.json(), "Токен доступа не найден в ответе"

    @allure.step("Авторизация с неверным паролем")
    def test_login_with_wrong_password(self, create_user):
        """Тест на авторизацию с неверным паролем"""
        user_data = create_user
        login_user = LoginUser()
        response = login_user.login(user_data["email"], "wrong_password")

        with allure.step("Проверка ответа на неверный пароль"):
            assert response.status_code == 401, f"Ожидался код ответа 401, но получен {response.status_code}"
            assert response.json().get("message") == "email or password are incorrect"

    @allure.step("Авторизация с неверным email")
    def test_login_with_wrong_email(self):
        """Тест на авторизацию с неверным email"""
        login_user = LoginUser()
        response = login_user.login("non_existing_user@example.com", "12345678")

        with allure.step("Проверка ответа на неверный email"):
            assert response.status_code == 401, f"Ожидался код ответа 401, но получен {response.status_code}"
            assert response.json().get("message") == "email or password are incorrect"
