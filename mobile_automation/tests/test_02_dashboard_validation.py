"""
AUTO-02 — Dashboard Validation
Status: PASS
Execution Time: 1 passed in 4.93s
Details: Validates that Kredily Home dashboard is rendered and Home tab is displayed and selected.
"""

import time
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

def test_dashboard_validation():
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
        assert driver.current_package == "com.kredily.mobile"
        home = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Home")
        assert home.is_displayed()
        assert home.get_attribute("selected") == "true"
        print("\nAUTO-02 PASSED: Kredily Home dashboard validated.")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_dashboard_validation()
