import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ElementHelpers:
    @staticmethod
    def wait_for_element(driver, locator, timeout=15):
        if not driver:
            return None
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

    @staticmethod
    def click_when_ready(driver, locator, timeout=15):
        if not driver:
            return False
        element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()
        return True

    @staticmethod
    def get_text_safe(driver, locator, timeout=10):
        if not driver:
            return ""
        try:
            element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
            return element.text
        except Exception:
            return ""
