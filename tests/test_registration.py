import pytest
from selenium.webdriver.common.by import By
from locators import RegisterPageLocators, MainPageLocators, LoginPageLocators, CommonLocators
from conftest import generate_email
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestRegistration:
    
    def test_successful_registration(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Дмитрий")
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys("d159753")
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))
        assert '/login' in driver.current_url

    def test_failed_registration_with_invalid_password(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Дмитрий")
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys("15975")
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        assert driver.find_element(*CommonLocators.INVALID_PASSWORD_MESSAGE).is_displayed()
        