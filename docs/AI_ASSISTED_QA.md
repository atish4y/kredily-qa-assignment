# AI-Assisted QA Documentation

This document records the utilization of **Artificial Intelligence (ChatGPT)** to accelerate and enhance mobile test automation during the QA evaluation of the **Kredily HRMS Android Mobile Application (`kredily-mobile-v2.apk`)**.

---

## 🤖 Overview of AI Assistance

- **AI Tool Used**: OpenAI ChatGPT
- **Testing / Automation Activity**: Converting manual dashboard validation test requirements into an executable Appium + Python + UiAutomator2 mobile automation test (`AUTO-02 — Dashboard Validation`).

---

## 1. Objective

Accelerate the creation of reliable mobile automation scripts by leveraging ChatGPT to scaffold the initial test structure, driver capabilities, and UI element verification logic for the Kredily HRMS Android application running on a BlueStacks Android emulator.

---

## 2. Prompt Used

```text
Create an Appium Python automation test for the Kredily HRMS Android APK that validates the Home dashboard. The test should connect to the BlueStacks emulator, verify that the Kredily package is running, locate the Home tab using an accessibility ID, verify that it is displayed and selected, and report the test result.
```

---

## 3. AI-Generated Output

The AI generated the initial `AUTO-02` test structure incorporating:
- Python 3 with `Appium-Python-Client`
- `UiAutomator2Options` driver configuration
- BlueStacks device identifier: `emulator-5554`
- App package: `com.kredily.mobile`
- App activity: `.MainActivity`
- `no_reset = True` session preservation
- Element locator via Accessibility ID: `"Home"`
- Assertions checking visibility and selected state

### Generated Automation Logic:

```python
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

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    try:
        assert driver.current_package == "com.kredily.mobile"
        home = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Home")
        assert home.is_displayed()
        assert home.get_attribute("selected") == "true"
        print("AUTO-02 PASSED: Kredily Home dashboard validated.")
    finally:
        driver.quit()
```

---

## 4. What Was Changed & Validated by Human QA Engineer

1. **Environment Configuration**:
   - Configured the actual BlueStacks Android emulator instance (`emulator-5554` on Android 11) and launched the Appium 2.x server on `http://127.0.0.1:4723`.
   - Verified that UiAutomator2 driver was properly installed and bound to the host ADB daemon.

2. **Package & Activity Verification**:
   - Confirmed the target package `com.kredily.mobile` and main entry activity `com.kredily.mobile.MainActivity` against the APK manifest using ADB tools.

3. **Selector Inspection**:
   - Validated the `"Home"` accessibility selector using Appium Inspector on the live BlueStacks session, ensuring the accessibility node was interactive and exposed the `selected` attribute.

4. **Execution & Timing Validation**:
   - Executed the generated test script against the active Kredily session.
   - Result: **1 passed in 4.93 seconds**. The test confirmed that the Kredily Home dashboard loaded with the Home tab visible and selected.

5. **Expansion to Core Workflows**:
   - The verified AI-assisted foundation was systematically extended to author the remaining automation journeys:
     - `AUTO-03`: Attendance anomaly to correction request workflow.
     - `AUTO-04`: Approval rejection with reason validation (which successfully caught defect **BUG-009**).
     - `AUTO-05`: Employee Directory search and profile inspection.

6. **Defect & Limitation Integrity**:
   - Transparently documented automation limitations rather than masking them: `AUTO-01` (Login form automation) was formally classified as **BLOCKED** due to UiAutomator2 element visibility constraints during clean session starts, avoiding false pass reports.

---

## 5. Conclusion

Leveraging AI for script scaffolding reduced initial automation setup time by over 60%, allowing the QA engineer to focus on locator refinement, timing synchronizations, and genuine defect discovery across critical HRMS workflows.
