import pytest
from selenium.webdriver.common.by import By
from locators import RegisterPageLocators, MainPageLocators, LoginPageLocators, MainPageHeaderLocators, CommonLocators, PasswordRecoveryPageLocators
from test_data import TEST_EMAIL, TEST_PASSWORD
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from urls import BASE_URL, REGISTER_URL


class TestLogin:
    def test_successful_login_from_main_page(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*CommonLocators.EMAIL_INPUT).send_keys(TEST_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()

    def test_successful_login_via_profile_button(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*MainPageHeaderLocators.ACCOUNT_LINK).click()
        driver.find_element(*CommonLocators.EMAIL_INPUT).send_keys(TEST_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()

    def test_successful_login_through_registration_form(self, driver):
        driver.get(REGISTER_URL)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RegisterPageLocators.LOGIN_LINK))
        driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()
        driver.find_element(*CommonLocators.EMAIL_INPUT).send_keys(TEST_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()

    def test_successfil_login_after_password_reset(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.PASSWORD_RESET).click()
        driver.find_element(*PasswordRecoveryPageLocators.LOGIN_LINK).click()
        driver.find_element(*CommonLocators.EMAIL_INPUT).send_keys(TEST_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()
