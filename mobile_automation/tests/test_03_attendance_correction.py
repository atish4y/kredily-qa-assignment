"""
AUTO-03 — Attendance Anomaly to Correction Request
Status: PASS
Execution Time: 1 passed in 23.62s
Details: Navigates from Home anomaly shortcut to Correction form, sets exact times,
enters approver reason, applies correction, and verifies confirmation dialog.
"""

import time
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

def test_attendance_correction_request():
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
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Home").click()
        time.sleep(3)
        driver.find_element(AppiumBy.XPATH, "//*[contains(@content-desc, 'anomaly to fix')]").click()
        time.sleep(2)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Request correction").click()
        time.sleep(2)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Set exact time").click()
        time.sleep(2)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "9:30 AM, \uf5de").click()
        time.sleep(1)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "6:30 PM, \uf5de").click()
        time.sleep(1)
        reason = driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Write your reason (visible to approver)']")
        reason.send_keys("Automation test - attendance correction")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Apply").click()
        time.sleep(3)
        confirmation = driver.find_element(AppiumBy.ID, "com.kredily.mobile:id/alert_title")
        assert confirmation.text == "Correction requested"
        print("\nAUTO-03 PASSED: Attendance correction requested successfully.")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_attendance_correction_request()
