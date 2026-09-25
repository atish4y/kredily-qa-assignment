from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15

    def find_element(self, locator):
        if not self.driver:
            return None
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator):
        if not self.driver:
            return False
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
        return True

    def send_keys(self, locator, text):
        if not self.driver:
            return False
        element = self.find_element(locator)
        if element:
            element.clear()
            element.send_keys(text)
            return True
        return False

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text if element else ""
