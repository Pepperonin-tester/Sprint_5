from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Кнопка "Оформить заказ"
    ORDER_BUTTON = (By.CLASS_NAME, "button_button_type_primary__1O7Bx")

class ConstructorPageLocators:
    # Вкладка "Булки" — уникальных атрибутов нет, поэтому использовал XPath по тексту span
    BUNS_TAB = (By.XPATH, "//div[contains(@class,'tab_tab__1SPyG') and .//span[text()='Булки']]")
    # Вкладка "Соусы" — уникальных атрибутов нет, поэтому использовал XPath по тексту span
    SAUCES_TAB = (By.XPATH, "//div[contains(@class,'tab_tab__1SPyG') and .//span[text()='Соусы']]")
    # Вкладка "Начинки" — уникальных атрибутов нет, поэтому использовал XPath по тексту span
    FILLINGS_TAB = (By.XPATH, "//div[contains(@class,'tab_tab__1SPyG') and .//span[text()='Начинки']]")

class LoginPageLocators:
    # Поле для ввода пароля
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    # Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # Ссылка "Зарегистрироваться"
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    # Ссылка "Восстановить пароль"
    PASSWORD_RESET = (By.XPATH, "//a[text()='Восстановить пароль']")

class AccountPageLocators:
    # Кнопка "Выход"
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".Account_button__14Yp3")

class RegisterPageLocators:
    # Поле для ввода имени
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    # Поле для ввода email
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Поле для ввода пароля
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # Ссылка "Войти"
    LOGIN_LINK = (By.XPATH, "//a[contains(@class, 'Auth_link__1fOlj')]")

class PasswordRecoveryPageLocators:
    # Кнопка "Восстановить пароль"
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    # Ссылка "Войти"
    LOGIN_LINK = (By.XPATH, "//a[contains(@class, 'Auth_link__1fOlj')]")

class MainPageHeaderLocators:
    # Логотип сайта
    LOGO = (By.XPATH, "//div[contains(@class,'logo')]/a")
    # Ссылка на страницу "Конструктор"
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']/..")
    # Ссылка на страницу "Лента заказов"
    ORDERS_LINK = (By.XPATH, "//p[text()='Лента заказов']/..")
    # Ссылка на страницу "Личный кабинет"
    ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']/..")

class CommonLocators:
    # Сообщение "Некорректный пароль"
    INVALID_PASSWORD_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']")
    # Поле для ввода email
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
