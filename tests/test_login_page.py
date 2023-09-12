import unittest
from .base_test import BaseTest
from pages.login_page import LoginPage
from time import sleep
import json


class TestLoginPage(BaseTest):
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.navigate_url("https://www.saucedemo.com/")

        with open("./resources/dataLogin.json") as data:
            fileData = json.load(data)

        for val in fileData:
            login_page.enter_username(val["username"])
            sleep(3)
            login_page.enter_password(val["password"])
            sleep(3)
            login_page.click_login_button()

            get_title = login_page.get_title()

            if get_title == "Swag Labs":
                login_page.get_message("Swag Labs", get_title)

                # urlWebsite = setup.current_url
                # assert urlWebsite == "https://www.saucedemo.com/inventory.html"
            # else:
                # login_page.get_message("Swag Las", get_text)
                # errorMessage = setup.find_element(
                #     By.CSS_SELECTOR, "h3[data-test='error']").text
                # assert errorMessage == message
                # else:
                #     login_page.error_message(expected)

                # self.assertEqual(actual_title, expected_title,
                #                  "Judul halaman tidak ada")

            sleep(5)


if __name__ == "__main__":
    unittest.main()
