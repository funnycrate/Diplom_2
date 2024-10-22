import pytest
import requests
from endpoints.register import RegisterUser
from endpoints.login import LoginUser
from endpoints.delete import DeleteUser
from data import *
from endpoints.order import CreateOrder


@pytest.fixture(scope="function")
def create_user(get_user_token):
    """Создает уникального пользователя перед тестом и удаляет его после."""
    user_data = generate_user_data()

    delete_user = DeleteUser()

    # Регистрация нового пользователя
    url = f"{BASE_URL}/auth/register"
    response = requests.post(url, json=user_data)
    assert response.status_code == 200, f"Ошибка при регистрации пользователя: {response.status_code}, {response.text}"

    yield user_data

    # Если email был изменён, используем новый email для получения токена
    email_to_use = user_data.get("new_email", user_data["email"])
    token = get_user_token(email_to_use, user_data["password"])

    # Удаление пользователя
    delete_response = delete_user.delete(token)
    assert delete_response.status_code == 202, f"Ошибка при удалении пользователя: {delete_response.status_code}, {delete_response.text}"


@pytest.fixture
def get_user_token():
    """Получение токена для авторизованного пользователя."""
    def _get_token(email, password):
        login_user = LoginUser()  # Создаем экземпляр класса для авторизации
        response = login_user.login(email, password)
        assert response.status_code == 200, f"Ошибка при авторизации пользователя: {response.status_code}, {response.text}"
        return response.json().get("accessToken")
    return _get_token

@pytest.fixture(scope="function")
def unique_email():
    """Фикстура для генерации уникального email"""
    return fake.unique.email()

@pytest.fixture
def get_ingredients():
    """Фикстура для получения списка ингредиентов"""
    create_order = CreateOrder()
    ingredients_response = create_order.get_ingredients()
    assert ingredients_response.status_code == 200, f"Не удалось получить список ингредиентов: {ingredients_response.text}"
    ingredients = [ingredient["_id"] for ingredient in ingredients_response.json()["data"]]
    return ingredients
