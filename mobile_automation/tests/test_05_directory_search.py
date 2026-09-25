import time

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

        time.sleep(4)

        print("\nAUTO-05: Home dashboard opened.")

        # =========================================================
        # STEP 2: Open Directory
        # =========================================================

        directory = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (
                    AppiumBy.XPATH,
                    '//android.widget.Button[@content-desc="Directory"]'
                )
            )
        )

        assert directory.is_displayed()
        directory.click()

        time.sleep(3)

        print("AUTO-05 STEP 1 PASSED: Directory opened.")

        # =========================================================
        # STEP 3: Search for employee
        # =========================================================

        search = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (
                    AppiumBy.XPATH,
                    '//android.widget.EditText[@resource-id="dir-q"]'
                )
            )
        )

        assert search.is_displayed()

        search.click()
        search.send_keys("QA Assesment")

        time.sleep(3)

        print("AUTO-05 STEP 2 PASSED: Employee search performed.")

        # =========================================================
        # STEP 4: Verify employee appears
        # =========================================================

        employee = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (
                    AppiumBy.XPATH,
                    '//android.widget.Button[@content-desc="Open QA Assesment"]'
                )
            )
        )

        assert employee.is_displayed()

        print("AUTO-05 STEP 3 PASSED: Employee result found.")

        # =========================================================
        # STEP 5: Open employee profile
        # =========================================================

        employee.click()

        time.sleep(4)

        print("AUTO-05 STEP 4 PASSED: Employee profile opened.")

        # =========================================================
        # STEP 6: Verify profile
        # =========================================================

        page_source = driver.page_source

        assert "QA Assesment" in page_source

        print("AUTO-05 STEP 5 PASSED: Employee profile validated.")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_directory_search_profile()
