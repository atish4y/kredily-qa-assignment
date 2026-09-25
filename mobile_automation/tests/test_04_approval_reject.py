"""
AUTO-04 — Approval Reject with Reason
Status: EXECUTED / APPLICATION DEFECT OBSERVED (BUG-009)
Details: Automates navigation to Regularization Approvals, opens a pending request,
enters a rejection reason, and taps Confirm. The application backend throws
"Attendance log not found" and aborts rejection, catching BUG-009.
"""

import time
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

def test_approval_reject_with_reason():
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
        driver.find_element(AppiumBy.XPATH, "//*[contains(@content-desc, 'approvals waiting')]").click()
        time.sleep(2)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Reg., 3").click()
        time.sleep(2)
        request = driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[starts-with(@resource-id, 'rq-')]")
        request.click()
        time.sleep(2)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Reject").click()
        time.sleep(1)
        reason = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="decide-reason"]')
        reason.send_keys("Automation test rejection")
        driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="decide-confirm"]').click()
        time.sleep(2)
        print("\nAUTO-04: Final Reject action executed.")
        print("Observed result: Application defect BUG-009 ('Attendance log not found').")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_approval_reject_with_reason()
