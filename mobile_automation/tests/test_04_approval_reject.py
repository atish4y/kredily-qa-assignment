import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_approval_rejection_workflow():

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"
    options.udid = "emulator-5554"
    options.app_package = "com.kredily.mobile"
    options.app_activity = ".MainActivity"
    options.no_reset = True

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    try:
        assert driver.current_package == "com.kredily.mobile"

        # =========================================================
        # STEP 1: Open Home
        # =========================================================

        home = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, "Home")
            )
        )

        assert home.is_displayed()
        home.click()

        time.sleep(5)

        print("\nAUTO-04: Home dashboard opened.")

        # =========================================================
        # STEP 2: Open Approvals
        # =========================================================

        approvals = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (
                    AppiumBy.XPATH,
                    "//android.widget.Button[contains(@content-desc, 'approvals waiting')]"
                )
            )
        )

        assert approvals.is_displayed()
        approvals.click()

        time.sleep(3)

        print("AUTO-04 STEP 1 PASSED: Approvals opened.")

        # =========================================================
        # STEP 3: Open Reg. requests
        # =========================================================

        reg_tab = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, "Reg., 3")
            )
        )

        assert reg_tab.is_displayed()
        reg_tab.click()

        time.sleep(3)

        print("AUTO-04 STEP 2 PASSED: Reg. requests opened.")

        # =========================================================
        # STEP 4: Find correction request
        # =========================================================

        request_card = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (
                    AppiumBy.XPATH,
                    "//android.view.ViewGroup[starts-with(@resource-id, 'rq-')]"
                )
            )
        )

        assert request_card.is_displayed()

        print("AUTO-04 STEP 3 PASSED: Correction request found.")

        # =========================================================
        # STEP 5: Open Reject action
        # =========================================================

        reject_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, "Reject")
            )
        )

        assert reject_button.is_displayed()
        reject_button.click()

        time.sleep(2)

        print("AUTO-04 STEP 4 PASSED: Reject action opened.")

        # =========================================================
        # STEP 6: Enter rejection reason
        # =========================================================

        reason = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (
                    AppiumBy.XPATH,
                    '//android.widget.EditText[@resource-id="decide-reason"]'
                )
            )
        )

        assert reason.is_displayed()

        reason.click()
        reason.send_keys(
            "Correction details could not be verified."
        )

        print("AUTO-04 STEP 5 PASSED: Rejection reason entered.")

        # =========================================================
        # STEP 7: Confirm rejection
        # =========================================================

        confirm_reject = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (
                    AppiumBy.XPATH,
                    '//android.widget.Button[@resource-id="decide-confirm"]'
                )
            )
        )

        assert confirm_reject.is_displayed()
        assert confirm_reject.is_enabled()

        confirm_reject.click()

        time.sleep(3)

        print("AUTO-04 STEP 6 PASSED: Rejection confirmed.")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_approval_rejection_workflow()
