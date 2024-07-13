import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN = "login"
PASSWORD = "password"


class TestAuthorizationYandex(unittest.TestCase):

    def __init__(self):
        self.browser = webdriver.Chrome(
            executable_path="/Users/artur/Desktop/ДЗ/Профессиональная работа с Python/chromedriver"
        )

    def login(self):
        self.browser.find_element_by_xpath(
            '//input[@data-t="fielfd:input-login"]'
        ).send_keys(LOGIN)
        self.browser.find_element_by_xpath('//button[@data-t="button:action"]').click()

    def password(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//input[@data-t="fielfd:input-passwd"]')
            )
        )
        self.browser.find_element_by_xpath(
            '//input[@data-t="fielfd:input-passwd"]'
        ).send_keys(PASSWORD)
        self.browser.find_element_by_xpath(
            '//button[@data-t="button:action:passp:sinf-in"]'
        ).click()

        self.assertIn("https://id.yandex.ru/", self.browser.title)

        self.browser.close()


if __name__ == "__main__":
    unittest.main()
