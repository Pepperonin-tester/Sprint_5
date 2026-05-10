import random

def generate_email():
    random_number = random.randint(100, 999)
    return f"skvortsov_dima_45_{random_number}@yandex.ru"

def generate_password():
    random_number = random.randint(1000, 9999)
    return f"password_{random_number}"

TEST_EMAIL = "SkvortsovDima_45_1998@yandex.ru"
TEST_PASSWORD = "d159753"