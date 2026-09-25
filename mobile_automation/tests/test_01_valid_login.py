"""
AUTO-01 — Valid Login
Status: BLOCKED / AUTOMATION LIMITATION
Details: UiAutomator2 connected to the correct package/activity but did not expose
login fields in the fresh automation session even though fields were visible in
Appium Inspector. Transparently reported as an automation limitation.
"""

import getpass
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

@pytest.mark.skip(reason="UiAutomator2 login-field visibility limitation during automated session launch")
def test_valid_login():
    password = getpass.getpass("Enter test password: ")
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"
    options.udid = "emulator-5554"
    options.app_package = "com.kredily.mobile"
    options.app_activity = ".MainActivity"
    options.no_reset = True

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    try:
        email = driver.find_element(AppiumBy.ID, "auth-ident")
        password_field = driver.find_element(AppiumBy.ID, "auth-pass")
        sign_in = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Sign in")
        email.send_keys("peoplekredily1@yopmail.com")
        password_field.send_keys(password)
        sign_in.click()
    finally:
        driver.quit()

if __name__ == "__main__":
    test_valid_login()
