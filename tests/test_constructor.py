import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from locators import ConstructorPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestConstructor:
    def test_navigate_to_buns(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*ConstructorPageLocators.SAUCES_TAB).click()
        driver.find_element(*ConstructorPageLocators.BUNS_TAB).click()
        buns_tab = driver.find_element(*ConstructorPageLocators.BUNS_TAB)
        assert 'tab_tab_type_current' in buns_tab.get_attribute('class')

    def test_navigate_to_sauces(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*ConstructorPageLocators.SAUCES_TAB).click()
        sauces_tab = driver.find_element(*ConstructorPageLocators.SAUCES_TAB)
        assert 'tab_tab_type_current' in sauces_tab.get_attribute('class')

    def test_navigate_to_fillings(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*ConstructorPageLocators.FILLINGS_TAB).click()
        fillings_tab = driver.find_element(*ConstructorPageLocators.FILLINGS_TAB)
        assert 'tab_tab_type_current' in fillings_tab.get_attribute('class')
        