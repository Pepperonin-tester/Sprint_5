import pytest
from selenium.webdriver.common.by import By
from locators import RegisterPageLocators, MainPageLocators, LoginPageLocators, MainPageHeaderLocators, PasswordRecoveryPageLocators
from conftest import TEST_EMAIL, TEST_PASSWORD
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogin:
    def test_successful_login_from_main_page(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()

    def test_successful_login_via_profile_button(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*MainPageHeaderLocators.ACCOUNT_LINK).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()

    def test_successful_login_through_registration_form(self, driver):
        driver.get("https://stellarburgers.education-services.ru/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RegisterPageLocators.LOGIN_LINK))
        driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()

    def test_successfil_login_after_password_reset(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.PASSWORD_RESET).click()
        driver.find_element(*PasswordRecoveryPageLocators.LOGIN_LINK).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()
