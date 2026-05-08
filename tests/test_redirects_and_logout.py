import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from locators import MainPageLocators, LoginPageLocators, MainPageHeaderLocators, AccountPageLocators
from conftest import TEST_EMAIL, TEST_PASSWORD, driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRedirects:

    def test_redirect_to_personal_account(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()
        driver.find_element(*MainPageHeaderLocators.ACCOUNT_LINK).click()
        assert '/account' in driver.current_url

    def test_redirect_from_personal_account_to_constructor(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()
        driver.find_element(*MainPageHeaderLocators.ACCOUNT_LINK).click()
        driver.find_element(*MainPageHeaderLocators.CONSTRUCTOR_LINK).click()
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()

    def test_logo_click_redirects_from_personal_account_to_constructor(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()
        driver.find_element(*MainPageHeaderLocators.ACCOUNT_LINK).click()
        driver.find_element(*MainPageHeaderLocators.LOGO).click()
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()

class TestLogout:
    def test_user_logout(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()
        driver.find_element(*MainPageHeaderLocators.ACCOUNT_LINK).click()
        assert '/account' in driver.current_url
        wait = WebDriverWait(driver, 10)
        logout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".Account_button__14Yp3")))
        logout_button.click()
        wait.until(EC.url_contains('/login'))
        assert '/login' in driver.current_url
        