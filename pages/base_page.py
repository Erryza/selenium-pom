
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    def enter_el_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def get_el_title(self):
        return self.driver.title

    def get_el_text(self, locator):
        element = self.wait_for_element(locator)
        element.text

    def get_el_message(self, actual, expected):
        self.assertEqual(actual, expected,
                         "Judul halaman tidak ada")
