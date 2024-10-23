import allure
from endpoints.register import RegisterUser
from data import generate_user_data

@allure.feature('Управление пользователями')
@allure.story('Регистрация, удаление и проверка пользователя')
class TestUserRegistration:

    @allure.step("Проверка уникального пользователя")
    def test_create_unique_user(self, create_user):
        """Тест на проверку успешного создания уникального пользователя"""
        user_data = create_user

        with allure.step("Проверка данных пользователя"):
            assert user_data["email"] is not None, "Email пользователя должен быть заполнен"
            assert user_data["password"] is not None, "Пароль пользователя должен быть заполнен"
            assert user_data["name"] is not None, "Имя пользователя должно быть заполнено"

    @allure.step("Попытка создать уже зарегистрированного пользователя")
    def test_create_existing_user(self, create_user):
        """Тест на создание пользователя, который уже существует"""
        register_user = RegisterUser()
        response = register_user.create_user(create_user)

        with allure.step("Проверка ответа"):
            assert response.status_code == 403, f"Ожидался код ответа 403, но получен {response.status_code}"
            assert response.json().get("message") == "User already exists"

    @allure.step("Попытка создать пользователя без пароля")
    def test_create_user_missing_password(self):
        """Тест на создание пользователя без пароля"""
        user_data = generate_user_data()  # Генерация уникальных данных
        del user_data["password"]  # Удаляем поле password

        register_user = RegisterUser()
        response = register_user.create_user(user_data)

        with allure.step("Проверка ответа"):
            assert response.status_code == 403, f"Ожидался код ответа 403, но получен {response.status_code}"
            assert response.json().get("message") == "Email, password and name are required fields"
