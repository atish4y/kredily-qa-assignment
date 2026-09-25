"""
AUTO-01 — Valid Login
Status: BLOCKED
Reason: UiAutomator2 successfully connected to the Kredily application, but the login fields
were not exposed to the fresh UiAutomator2 Python session/page source, despite being visible
in Appium Inspector.
Manual login flow was verified separately.
The automated login test did NOT successfully execute.
"""

from getpass import getpass
import time
import pytest

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


@pytest.mark.skip(reason="BLOCKED: Login fields not exposed to fresh UiAutomator2 session")
def test_valid_login():
    """
    Attempted automation artifact for AUTO-01.
    Retained for documentation of the automation attempt and UiAutomator2 limitation.
    """
    email_address = "peoplekredily1@yopmail.com"
    password = getpass("Enter your Kredily password: ")

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"
    options.udid = "emulator-5554"
    options.app_package = "com.kredily.mobile"
    options.app_activity = ".MainActivity"
    options.no_reset = False

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    try:
        email = driver.find_element(AppiumBy.ID, "auth-ident")
        email.clear()
        email.send_keys(email_address)

        password_field = driver.find_element(AppiumBy.ID, "auth-pass")
        password_field.clear()
        password_field.send_keys(password)

        sign_in = driver.find_element(
            AppiumBy.ACCESSIBILITY_ID,
            "Sign in"
        )
        sign_in.click()

        time.sleep(5)

        assert driver.current_package == "com.kredily.mobile"
        print("AUTO-01 attempted execution finished.")
    finally:
        driver.quit()


if __name__ == "__main__":
    print("AUTO-01 Status: BLOCKED (UiAutomator2 login-field visibility limitation)")
    test_valid_login()
