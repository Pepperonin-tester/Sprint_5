import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver  

    driver.quit()

import random

def generate_email():
    random_number = random.randint(100, 999)
    return f"skvortsov_dima_45_{random_number}@yandex.ru"


TEST_EMAIL = "SkvortsovDima_45_1998@yandex.ru"
TEST_PASSWORD = "d159753"