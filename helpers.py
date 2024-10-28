from faker import Faker
from datetime import datetime


fake = Faker()

def generate_user_data():
    """Генерирует данные пользователя с уникальным email и статичным паролем."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    unique_email = f"{fake.user_name()}_{timestamp}@example.com"
    return {
        "email": unique_email,
        "password": "12345678",
        "name": fake.first_name()
    }

def generate_unique_email():
    """Генерирует уникальный email."""
    return fake.unique.email()