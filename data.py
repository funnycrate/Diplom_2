from faker import Faker
from datetime import datetime


fake = Faker()

BASE_URL = "https://stellarburgers.nomoreparties.site/api"

def generate_user_data():
    """Генерирует данные пользователя с уникальным email и статичным паролем."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    unique_email = f"{fake.user_name()}_{timestamp}@example.com"
    return {
        "email": unique_email,
        "password": "12345678",  # Оставляем фиксированный пароль
        "name": fake.first_name()
    }

