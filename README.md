# Kredily HRMS – QA Assessment & Mobile Automation Deliverable

[![QA Manual & Automation](https://img.shields.io/badge/QA-Manual%20%26%20Mobile%20Automation-blue.svg)](https://github.com/atish4y)
[![Appium UiAutomator2](https://img.shields.io/badge/Mobile-Appium%20%2B%20Python-green.svg)](https://appium.io/)
[![Target](https://img.shields.io/badge/Target-Kredily%20HRMS%20APK-purple.svg)](https://kredily.com)

This repository contains the Quality Assurance assessment deliverable for the **Kredily HRMS Android Mobile Application (`kredily-mobile-v2.apk`)**.

---

## 📌 Table of Contents
1. [Overview & Test Environment](#-overview--test-environment)
2. [Functional Testing (20 Test Cases)](#1-functional-testing)
3. [Bug Reporting (9 Genuine Bugs)](#2-bug-reporting)
4. [Mobile Automation (5 User Journeys)](#3-mobile-automation)
5. [Automation Execution Report](#4-automation-execution-report)
6. [AI-Assisted QA Documentation](#5-ai-assisted-qa)
7. [Test Evidence & Screenshots](#6-test-evidence--screenshots)
8. [QA Summary & Deliverables](#7-qa-summary--deliverables)
9. [Setup & Execution Guide](#8-setup--execution-guide)

---

## 📱 Overview & Test Environment

- **Target Application**: Kredily HRMS Android APK (`kredily-mobile-v2.apk`, Package: `com.kredily.mobile`, Activity: `.MainActivity`)
- **Execution Platform**: BlueStacks 5 Android Emulator (`emulator-5554`, Android 11, x86_64)
- **Appium Server**: Appium 2.x on `http://127.0.0.1:4723` (UiAutomator2 Driver)
- **Test Credentials**: `peoplekredily1@yopmail.com`
- **Scope Covered**: Attendance, Attendance Correction/Regularization, Approvals & Rejections, Employee Directory, Profile Management, Personal Information, Education, Family Members, Emergency Contacts, Digital ID Card, Company Setup, Leave Setup, and Holiday Calendar.

> [!NOTE]
> **API Testing Status**: API Testing was investigated but not completed due to the inability to establish a reliable authenticated API testing environment. No unverified API results are included.

---

## 1. FUNCTIONAL TESTING

### Summary: 20 Test Cases (Positive, Negative, Edge)

| TC ID | Workflow / Module | Type | Expected Result | Actual Result | Status | Bug Ref |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: |
| **TC-001** | Attendance / Correction Requests | Positive | Request details open successfully | Request details opened successfully | **PASS** | — |
| **TC-002** | Attendance Correction (Empty Reason) | Negative | Submission blocked; reason required | Submission blocked until reason entered | **PASS** | — |
| **TC-003** | Attendance Out earlier than In time | Negative/Edge | Reject invalid sequence or require overnight | Accepted; Out time treated as next day | **FAIL** | **BUG-001** |
| **TC-004** | Home Fix Shortcut Navigation | Positive | Relevant anomaly screen opens | Anomaly opened | **PASS** | — |
| **TC-005** | Correction Request Status After Submit | Positive | Submitted/pending status displayed | Correction requested status displayed | **PASS** | — |
| **TC-006** | Approval Rejection without Reason | Negative | Rejection blocked until reason provided | Rejection reason was required | **PASS** | — |
| **TC-007** | Approvals Multi-Select | Edge | Multiple requests selectable | Multiple requests selected successfully | **PASS** | — |
| **TC-008** | Bulk Approve All / Reject Actions | Positive | Bulk action buttons appear | Action buttons appeared | **PASS** | — |
| **TC-009** | Open Employee Directory | Positive | Employee Directory opens | Directory opened | **PASS** | — |
| **TC-010** | Search Existing Employee | Positive | Matching employee appears | Employee appeared | **PASS** | — |
| **TC-011** | Search Nonexistent Employee | Negative/Edge | No matching employee displayed | No matching employee displayed | **PASS** | — |
| **TC-012** | Save Malformed Personal Email ("abc") | Negative | Invalid email rejected | Malformed email accepted | **FAIL** | **BUG-002** |
| **TC-013** | Personal Email with Internal Space | Negative | Invalid email rejected | Malformed email accepted | **FAIL** | **BUG-002** |
| **TC-014** | Save 9-digit Alternate Phone | Edge | Invalid-length number rejected | 9-digit value accepted/persisted | **FAIL** | **BUG-003** |
| **TC-015** | Save 12-digit Alternate Phone | Edge | Invalid-length number rejected | 12-digit value accepted/persisted | **FAIL** | **BUG-003** |
| **TC-016** | Empty Education Record Save | Negative | Empty education record prevented | Empty record created and saved | **FAIL** | **BUG-004** |
| **TC-017** | Add Family Member with Future DOB | Edge | Future DOB rejected | Future DOB accepted and saved | **FAIL** | **BUG-005** |
| **TC-018** | Emergency Contact 4-digit Phone | Negative | Invalid phone number rejected | 4-digit & alpha values accepted | **FAIL** | **BUG-006** |
| **TC-019** | Open Employee ID Card | Positive | Employee ID card opens | ID card opened | **PASS** | — |
| **TC-020** | Invite with Invalid 4-digit Mobile | Negative | Invalid mobile rejected | Rejected: "Phone number is not valid." | **PASS** | — |

Full test case details and execution steps: [`docs/TEST_CASES.md`](docs/TEST_CASES.md)

---

## 2. BUG REPORTING

### Summary of 9 Documented Bugs

| Bug ID | Title | Module | Severity | Related TC / Test | Evidence Screenshot |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **BUG-001** | Attendance correction accepts Out time earlier than In time | Attendance | **Medium** | TC-003 | Documented in TC-003 |
| **BUG-002** | Personal email validation accepts malformed email values (`ab   c@gmail.com`) | Profile | **Medium** | TC-012, TC-013 | `03_bug_002_bug_003_personal_info_validation.png` |
| **BUG-003** | Alternate phone field accepts invalid numeric lengths (`12345678`) | Profile | **Low** | TC-014, TC-015 | `03_bug_002_bug_003_personal_info_validation.png` |
| **BUG-004** | Empty education record can be created without mandatory fields | Profile | **Medium** | TC-016 | Documented in TC-016 |
| **BUG-005** | Future family-member Date of Birth (DOB) is accepted (`Jan 01, 2028`) | Profile | **Low** | TC-017 | `02_bug_005_bug_006_family_emergency_contacts.png` |
| **BUG-006** | Emergency contact phone field accepts alphabetic (`ahcd`) and 4-digit (`1234`) values | Profile | **Medium** | TC-018 | `02_bug_005_bug_006_family_emergency_contacts.png` |
| **BUG-007** | Holiday Calendar next-month navigation arrow is unresponsive | Profile / Calendar | **Low** | Exploratory | Documented in TC |
| **BUG-008** | Financial leave-year option is unresponsive during leave setup | Company Setup | **Medium** | Exploratory | `04_company_setup_configuration.png` |
| **BUG-009** | Attendance correction request cannot be rejected ("Attendance log not found") | Approvals | **High** | AUTO-04 | `05_bug_009_approvals_rejection_error.png` |

Full defect reports with reproduction steps: [`docs/BUG_REPORTS.md`](docs/BUG_REPORTS.md)

---

## 3. MOBILE AUTOMATION

- **Framework**: Appium + Python + UiAutomator2
- **Device**: BlueStacks Android emulator (`emulator-5554`)
- **Package**: `com.kredily.mobile`
- **Activity**: `com.kredily.mobile.MainActivity`
- **Appium Server**: `http://127.0.0.1:4723`

### AUTO-01 — Valid Login
- **Status**: BLOCKED
- **Reason**: UiAutomator2 successfully connected to the Kredily application, but the login fields were not exposed to the fresh UiAutomator2 Python session/page source, despite being visible in Appium Inspector.
- **Manual login flow**: Verified separately.
- **Automated test**: Did NOT successfully execute.

```python
"""
AUTO-01 — Valid Login (Attempted Automation Artifact)
Status: BLOCKED (UiAutomator2 login-field visibility limitation)
"""

from getpass import getpass
import time
import pytest

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


@pytest.mark.skip(reason="BLOCKED: Login fields not exposed to fresh UiAutomator2 session")
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
        print("AUTO-01 attempted execution finished.")
    finally:
        driver.quit()
```

### AUTO-02 — Dashboard Validation
- **Status**: PASS
- **Actual execution**: 1 passed in 4.93s

```python
import time

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
        # Verify Kredily is running
        assert driver.current_package == "com.kredily.mobile"

        # Find Home navigation button
        home = driver.find_element(
            AppiumBy.ACCESSIBILITY_ID,
            "Home"
        )

        # Verify Home is visible
        assert home.is_displayed()

        # Verify Home is the currently selected tab
        assert home.get_attribute("selected") == "true"

        print("\nAUTO-02 PASSED: Kredily Home dashboard validated.")

    finally:
        driver.quit()
```

### AUTO-03 — Attendance Anomaly to Correction Request
- **Status**: PASS
- **Actual execution**: 1 passed in 23.62s

```python
import time
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
    finally:
        driver.quit()
```

### AUTO-04 — Approval Rejection Workflow
- **Status**: EXECUTED / APPLICATION DEFECT OBSERVED
- **Observed behavior**:
  - The automation reached the final Reject action.
  - The application displayed the error: `"Attendance log not found"`.
  - The request was not rejected.
  - This corresponds to **BUG-009**.

```python
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

        # STEP 1: Open Home
        home = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Home"))
        )
        assert home.is_displayed()
        home.click()
        time.sleep(5)

        # STEP 2: Open Approvals
        approvals = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "//android.widget.Button[contains(@content-desc, 'approvals waiting')]")
            )
        )
        assert approvals.is_displayed()
        approvals.click()
        time.sleep(3)

        # STEP 3: Open Reg. requests
        reg_tab = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Reg., 3"))
        )
        assert reg_tab.is_displayed()
        reg_tab.click()
        time.sleep(3)

        # STEP 4: Find correction request
        request_card = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "//android.view.ViewGroup[starts-with(@resource-id, 'rq-')]")
            )
        )
        assert request_card.is_displayed()

        # STEP 5: Open Reject action
        reject_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Reject"))
        )
        assert reject_button.is_displayed()
        reject_button.click()
        time.sleep(2)

        # STEP 6: Enter rejection reason
        reason = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="decide-reason"]')
            )
        )
        assert reason.is_displayed()
        reason.click()
        reason.send_keys("Correction details could not be verified.")

        # STEP 7: Confirm rejection
        confirm_reject = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.Button[@resource-id="decide-confirm"]')
            )
        )
        assert confirm_reject.is_displayed()
        assert confirm_reject.is_enabled()
        confirm_reject.click()
        time.sleep(3)

        print("AUTO-04 STEP 6: Rejection confirmed action triggered.")
        # Note: Backend returns 'Attendance log not found' (BUG-009)
    finally:
        driver.quit()
```

### AUTO-05 — Directory Search and Employee Profile
- **Status**: PASS
- **Actual execution**: 1 passed in 19.06s

```python
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

        # STEP 1: Open Home
        home = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Home"))
        )
        assert home.is_displayed()
        home.click()
        time.sleep(4)

        # STEP 2: Open Directory
        directory = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Directory"]')
            )
        )
        assert directory.is_displayed()
        directory.click()
        time.sleep(3)

        # STEP 3: Search for employee
        search = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="dir-q"]')
            )
        )
        assert search.is_displayed()
        search.click()
        search.send_keys("QA Assesment")
        time.sleep(3)

        # STEP 4: Verify employee appears
        employee = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Open QA Assesment"]')
            )
        )
        assert employee.is_displayed()

        # STEP 5: Open employee profile
        employee.click()
        time.sleep(4)

        # STEP 6: Verify profile
        page_source = driver.page_source
        assert "QA Assesment" in page_source
        print("AUTO-05 STEP 5 PASSED: Employee profile validated.")
    finally:
        driver.quit()
```

---

## 4. AUTOMATION EXECUTION REPORT

| Test ID | Journey Name | Status | Execution Time | Outcome / Notes |
| :---: | :--- | :---: | :---: | :--- |
| **AUTO-01** | Valid Login | **BLOCKED** | — | UiAutomator2 connected, but login fields not exposed in fresh session. Manual flow verified separately; automated test did not execute successfully. |
| **AUTO-02** | Dashboard Validation | **PASS** | 4.93s | Successfully validated Home tab accessibility ID & selected state. |
| **AUTO-03** | Attendance Correction Request | **PASS** | 23.62s | Anomaly navigation → Set time 9:30-6:30 → Applied → Confirmed. |
| **AUTO-04** | Approval Rejection Workflow | **EXECUTED / DEFECT OBSERVED** | 14.21s | Reached final Reject; exposed backend error **BUG-009** (*"Attendance log not found"*). |
| **AUTO-05** | Directory Search & Profile | **PASS** | 19.06s | Searched "QA Assesment" → Opened profile card successfully. |

---

## 5. AI-ASSISTED QA

- **Tool Used**: ChatGPT
- **Testing / Automation Activity**:
  AI assistance was specifically used to create the initial mobile automation test, **AUTO-02 — Dashboard Validation**. The AI helped convert the manual dashboard validation requirement into an executable Appium + Python + UiAutomator2 test.

### Prompt Used:
> "Create an Appium Python automation test for the Kredily HRMS Android APK that validates the Home dashboard. The test should connect to the BlueStacks emulator, verify that the Kredily package is running, locate the Home tab using an accessibility ID, verify that it is displayed and selected, and report the test result."

### AI-Generated Output:
The AI generated the initial `AUTO-02` test structure using:
- Python & `Appium-Python-Client`
- `UiAutomator2Options` driver config
- BlueStacks device ID: `emulator-5554`
- Package: `com.kredily.mobile`
- Activity: `.MainActivity`
- Accessibility ID: `"Home"`
- Assertion that the Home tab is displayed and selected

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

### What I Changed / Validated:
- Configured the real BlueStacks emulator and Appium server rather than relying only on generated code.
- Verified the actual package name and activity used by the APK.
- Checked the "Home" selector in the running application / Appium Inspector.
- Executed the generated test against the actual Kredily APK: **1 passed in 4.93 seconds**.
- The output confirmed that the Kredily Home dashboard loaded and the Home tab was displayed and selected.
- Extended the same AI-assisted approach to additional journeys: attendance correction, approval rejection, and directory/profile search.
- Verified and fine-tuned locator synchronization with `WebDriverWait` across complex views.

Full AI-Assisted QA documentation: [`docs/AI_ASSISTED_QA.md`](docs/AI_ASSISTED_QA.md)

---

## 6. TEST EVIDENCE & SCREENSHOTS

Real mobile application screenshots captured from live testing on the BlueStacks Android emulator (`emulator-5554`, Android 11).

| File | Associated Tests / Bugs | Context & Observed Behavior |
| :--- | :--- | :--- |
| [`screenshots/01_dashboard_live_screen.png`](screenshots/01_dashboard_live_screen.png) | `AUTO-02`, `TC-004` | **Live Home Dashboard**: QA Assesment clocked in (`12:51:19`), shift tracking, and pending approvals alert banner (`"3 approvals waiting · 3 corrections"`). |
| [`screenshots/02_bug_005_bug_006_family_emergency_contacts.png`](screenshots/02_bug_005_bug_006_family_emergency_contacts.png) | `BUG-005`, `BUG-006`, `TC-017`, `TC-018` | **Profile Family & Emergency**: `BUG-005`: Future DOB `Jan 01, 2028` saved without validation. `BUG-006`: Emergency contact saved with 4-digit phone `1234` and alphabetic `ahcd`. |
| [`screenshots/03_bug_002_bug_003_personal_info_validation.png`](screenshots/03_bug_002_bug_003_personal_info_validation.png) | `BUG-002`, `BUG-003`, `TC-012`, `TC-013`, `TC-014` | **Profile Personal Info**: `BUG-002`: Malformed email with whitespace `ab   c@gmail.com` accepted. `BUG-003`: 8-digit alternate phone `12345678` accepted without 10-digit validation. |
| [`screenshots/04_company_setup_configuration.png`](screenshots/04_company_setup_configuration.png) | `TC-020`, `BUG-008` | **Company Setup Summary**: Displays initial configuration defaults and leave cycle locked to Calendar (Jan–Dec). |
| [`screenshots/05_bug_009_approvals_rejection_error.png`](screenshots/05_bug_009_approvals_rejection_error.png) | `BUG-009`, `AUTO-04`, `TC-006`, `TC-007`, `TC-008` | **Approvals Rejection Defect**: Multi-select of 3 regularization requests shows red error banner: `"3 couldn't be processed — Attendance log not found"`. |

Full screenshot catalog and analysis: [`screenshots/README.md`](screenshots/README.md)

---

## 7. QA SUMMARY & DELIVERABLES

- **Scope Covered**: Attendance, attendance correction/regularization, approvals, employee directory, employee profile, personal information, education, family members, emergency contacts, ID card, company setup, leave setup, holiday calendar.
- **Functional Testing**: 20 test cases created and executed covering positive, negative and edge scenarios (13 passed, 7 failed).
- **Bug Reporting**: 9 genuine bugs documented (1 High, 5 Medium, 3 Low). BUG-001 to BUG-006 directly observed; BUG-007 and BUG-008 exploratory findings; BUG-009 observed during approval rejection validation.
- **Automation**: 5 journeys evaluated with Appium & UiAutomator2. AUTO-02, AUTO-03 and AUTO-05 passed. AUTO-04 executed through to final rejection action and caught BUG-009. AUTO-01 was blocked by UiAutomator2 fresh-session visibility limitation.
- **Evidence**: 5 real screenshots documented with full context in `screenshots/`.
- **API Testing**: Investigated but not completed due to environment constraints; no unverified API results claimed.

Full summary report: [`docs/FINAL_QA_SUMMARY.md`](docs/FINAL_QA_SUMMARY.md)

---

## 8. SETUP & EXECUTION GUIDE

### Prerequisites
- Python 3.10+
- BlueStacks 5 (or Android Emulator) running on port 5554
- Appium 2.x server running:
  ```bash
  appium
  ```

### Install Dependencies
```bash
pip install -r mobile_automation/requirements.txt
```

### Run Mobile Automation Tests
```bash
# Standalone execution report
python mobile_automation/run_mobile_tests.py

# Or run tests via PyTest
pytest mobile_automation/tests/ -v
```
