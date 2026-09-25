"""
AUTO-05 — Directory Search and Employee Profile
Status: PASS
Execution Time: 1 passed in 19.06s
Details: Navigates to Directory, searches for employee "QA Assesment",
opens profile, and verifies employee details render successfully.
"""

import time
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_directory_search_profile():
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
        home = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Home"))
        )
        assert home.is_displayed()
        home.click()
        time.sleep(4)
        
        directory = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="Directory"]'))
        )
        directory.click()
        time.sleep(3)
        
        search = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="dir-q"]'))
        )
        search.click()
        search.send_keys("QA Assesment")
        time.sleep(3)
        
        employee = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="Open QA Assesment"]'))
        )
        assert employee.is_displayed()
        employee.click()
        time.sleep(4)
        
        assert "QA Assesment" in driver.page_source
        print("\nAUTO-05 PASSED: Employee directory search and profile verified.")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_directory_search_profile()
