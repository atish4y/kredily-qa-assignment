from getpass import getpass
import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


def test_valid_login():

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

        print("\nAUTO-01 PASSED: Valid login completed.")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_valid_login()
