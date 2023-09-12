from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    TITLE_LOGIN = (By.XPATH, "//div[@class='login_logo']")
    MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
