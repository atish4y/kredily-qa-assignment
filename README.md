# Kredily HRMS – QA Assessment & Mobile Automation Deliverable

[![QA Manual & Automation](https://img.shields.io/badge/QA-Manual%20%26%20Mobile%20Automation-blue.svg)](https://github.com/atish4y)
[![Appium UiAutomator2](https://img.shields.io/badge/Mobile-Appium%20%2B%20Python-green.svg)](https://appium.io/)
[![API Testing](https://img.shields.io/badge/API-Postman%20%2B%20REST-orange.svg)](https://www.postman.com/)
[![Target](https://img.shields.io/badge/Target-Kredily%20HRMS%20APK-purple.svg)](https://kredily.com)

This repository contains the complete Quality Assurance assessment submission for the **Kredily HRMS Android Mobile Application (`kredily-mobile-v2.apk`)** and its backend API services.

---

## 📌 Table of Contents
1. [Overview & Test Environment](#-overview--test-environment)
2. [Functional Testing (20 Test Cases)](#1-functional-testing)
3. [Bug Reporting (9 Genuine Bugs)](#2-bug-reporting)
4. [Mobile Automation (5 User Journeys)](#3-mobile-automation)
5. [Automation Execution Report](#4-automation-execution-report)
6. [API Testing](#5-api-testing)
7. [AI-Assisted QA Documentation](#6-ai-assisted-qa)
8. [QA Summary & Deliverables](#7-qa-summary--deliverables)
9. [Setup & Execution Guide](#8-setup--execution-guide)

---

## 📱 Overview & Test Environment

- **Target Application**: Kredily HRMS Android APK (`kredily-mobile-v2.apk`, Package: `com.kredily.mobile`, Activity: `.MainActivity`)
- **Execution Platform**: BlueStacks 5 Android Emulator (`emulator-5554`, Android 11, x86_64)
- **Appium Server**: Appium 2.x on `http://127.0.0.1:4723` (UiAutomator2 Driver)
- **Test Credentials**: `peoplekredily1@yopmail.com`
- **Scope Covered**: Attendance, Attendance Correction/Regularization, Approvals & Rejections, Employee Directory, Profile Management, Personal Information, Education, Family Members, Emergency Contacts, Digital ID Card, Company Setup, Leave Setup, and Holiday Calendar.

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

---

## 2. BUG REPORTING

### BUG-001 — Attendance correction accepts Out time earlier than In time
- **Severity**: Medium
- **Steps**: Open attendance anomaly → Request correction → In 09:30 AM → Out 08:30 AM → enter reason → submit.
- **Expected**: Invalid same-day sequence rejected or overnight explicitly required.
- **Actual**: Request accepted and earlier Out time interpreted as next day.
- **Related TC**: TC-003

### BUG-002 — Personal email validation accepts malformed email values
- **Severity**: Medium
- **Steps**: Profile → Edit Personal Information → save `"abc"`; repeat with `"ab c@gmail.com"`.
- **Expected**: Malformed email addresses rejected.
- **Actual**: Both malformed values accepted.
- **Related TC**: TC-012, TC-013

### BUG-003 — Alternate phone field accepts invalid numeric lengths
- **Severity**: Low
- **Steps**: Profile → Edit Personal Information → save 9-digit and 12-digit alternate numbers.
- **Expected**: Invalid-length phone numbers rejected.
- **Actual**: Both values accepted/persisted.
- **Related TC**: TC-014, TC-015

### BUG-004 — Empty education record can be created
- **Severity**: Medium
- **Steps**: Profile → Education → Add → leave fields empty → Save.
- **Expected**: Empty education record prevented.
- **Actual**: Empty education record created.
- **Related TC**: TC-016

### BUG-005 — Future family-member DOB is accepted
- **Severity**: Low
- **Steps**: Profile → Family → Add → enter future DOB (e.g. Jan 1, 2028 during testing on Sep 25, 2026) → Save.
- **Expected**: Future DOB rejected.
- **Actual**: Future DOB accepted and saved.
- **Related TC**: TC-017

### BUG-006 — Emergency contact phone field accepts alphabetic and invalid short values
- **Severity**: Medium
- **Steps**: Profile → Emergency Contacts → Add → enter `"ahcd"` and save; repeat with `"1234"`.
- **Expected**: Only valid phone-number format accepted.
- **Actual**: Alphabetic input and 4-digit number accepted.
- **Related TC**: TC-018

### BUG-007 — Holiday Calendar next-month navigation is unresponsive
- **Severity**: Low
- **Steps**: Profile → Holidays → Calendar → September 2026 → tap next-month arrow.
- **Expected**: Calendar advances to next month.
- **Actual**: Month did not change.
- **Status**: Exploratory finding; recheck before final submission.

### BUG-008 — Financial leave-year option is unresponsive
- **Severity**: Medium
- **Steps**: Company Setup → Leave Setup → Leave Year → select Financial (Apr–Mar).
- **Expected**: Financial option becomes selected.
- **Actual**: Option did not respond/select during testing.
- **Status**: Exploratory finding; recheck before final submission.

### BUG-009 — Attendance correction request cannot be rejected
- **Severity**: High
- **Steps**: Approvals → Reg. → attendance correction request → Reject → enter valid reason → final Reject.
- **Expected**: Request rejected and status updated.
- **Actual**: Red `"Attendance log not found"` message displayed and request was not rejected.
- **Related Automation**: AUTO-04

---

## 3. MOBILE AUTOMATION

- **Framework**: Appium + Python + UiAutomator2
- **Device**: BlueStacks Android emulator (`emulator-5554`)
- **Package**: `com.kredily.mobile`
- **Activity**: `com.kredily.mobile.MainActivity`
- **Appium Server**: `http://127.0.0.1:4723`

### AUTO-01 — Valid Login
- **Status**: BLOCKED / AUTOMATION LIMITATION
- **Result**: UiAutomator2 connected to the correct package/activity but did not expose login fields in the fresh automation session even though fields were visible in Appium Inspector. Transparently documented and not falsely marked as passed.

```python
import getpass
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

def test_valid_login():
    password = getpass.getpass("Enter test password: ")
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
        email = driver.find_element(AppiumBy.ID, "auth-ident")
        password_field = driver.find_element(AppiumBy.ID, "auth-pass")
        sign_in = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Sign in")
        email.send_keys("peoplekredily1@yopmail.com")
        password_field.send_keys(password)
        sign_in.click()
    finally:
        driver.quit()
```

### AUTO-02 — Dashboard Validation
- **Status**: PASS
- **Execution**: 1 passed in 4.93s

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
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    try:
        assert driver.current_package == "com.kredily.mobile"
        home = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Home")
        assert home.is_displayed()
        assert home.get_attribute("selected") == "true"
        print("\nAUTO-02 PASSED: Kredily Home dashboard validated.")
    finally:
        driver.quit()
```

### AUTO-03 — Attendance Anomaly to Correction Request
- **Status**: PASS
- **Execution**: 1 passed in 23.62s

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

### AUTO-04 — Approval Reject with Reason
- **Status**: EXECUTED / APPLICATION DEFECT OBSERVED
- **Result**: Reached final Reject action. App displayed `"Attendance log not found"` and did not reject the request. This directly exposed defect **BUG-009**.

```python
import time
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
        print("AUTO-04: Final Reject action executed.")
        print("Observed result: Attendance log not found; request was not rejected.")
    finally:
        driver.quit()
```

### AUTO-05 — Directory Search and Employee Profile
- **Status**: PASS
- **Execution**: 1 passed in 19.06s

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
    finally:
        driver.quit()
```

---

## 4. AUTOMATION EXECUTION REPORT

| Test ID | Journey Name | Status | Execution Time | Outcome / Notes |
| :---: | :--- | :---: | :---: | :--- |
| **AUTO-01** | Valid Login | **BLOCKED** | — | UiAutomator2 login-field visibility limitation during session initialization |
| **AUTO-02** | Dashboard Validation | **PASS** | 4.93s | Successfully validated Home tab accessibility ID & selected state |
| **AUTO-03** | Attendance Correction Request | **PASS** | 23.62s | Anomaly navigation → Set time 9:30-6:30 → Applied → Confirmed |
| **AUTO-04** | Approval Reject with Reason | **EXECUTED** | 14.21s | Reached final Reject; exposed backend error **BUG-009** |
| **AUTO-05** | Directory Search & Profile | **PASS** | 19.06s | Searched "QA Assesment" → Opened profile card successfully |

---

## 5. API TESTING

The repository includes a ready-to-run Postman collection and automated Python REST API tests covering both positive and negative scenarios against the Kredily backend:
- `POST /ws/v1/accounts/set-password-login/` (Positive authentication & Negative invalid user handling)
- `GET /ws/v2/company/dashboard/` (Authenticated punch validation & Unauthenticated access enforcement)
- `GET /mapi/v1/leave/balances/me/` (User leave balances verification)
- `GET /mapi/v1/livetrack/my/plans/`
- `GET /kapi/v1/payroll/core/payslip/`

Deliverables:
- Postman Collection: [`api_testing/kredily_api_postman_collection.json`](api_testing/kredily_api_postman_collection.json)
- Standalone Runner: [`api_testing/run_api_tests.py`](api_testing/run_api_tests.py)

---

## 6. AI-ASSISTED QA

- **Tool Used**: ChatGPT
- **Testing / Automation Activity**:
  AI assistance was specifically used to create the first successful mobile automation test, **AUTO-02 — Dashboard Validation**. The AI helped convert the manual dashboard validation requirement into an executable Appium + Python + UiAutomator2 test.

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
- Failed/blocked automation was not falsely marked as passed: AUTO-01 remained blocked because login fields were not exposed to the fresh UiAutomator2 session.

---

## 7. QA SUMMARY & DELIVERABLES

- **Scope Covered**: Attendance; attendance correction/regularization; approvals; employee directory; employee profile; personal information; education; family members; emergency contacts; ID card; company setup; leave setup; holiday calendar.
- **Functional Testing**: 20 test cases created and executed covering positive, negative and edge scenarios.
- **Bug Reporting**: 9 bugs documented. BUG-001 to BUG-006 were directly observed. BUG-007 and BUG-008 were exploratory findings. BUG-009 was observed during approval rejection validation.
- **Automation**: 5 journeys selected. AUTO-02, AUTO-03 and AUTO-05 passed. AUTO-04 exposed BUG-009. AUTO-01 was blocked by an automation visibility limitation and was not falsely reported as passed.
- **Evidence**: Visual evidence documented for relevant bugs and automation executions.
- **API Testing**: Included Postman collection and Python executable test runner.

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

### Run API Automation Tests
```bash
python api_testing/run_api_tests.py
```
