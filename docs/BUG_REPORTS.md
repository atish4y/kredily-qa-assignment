# Kredily HRMS Mobile Application - Defect / Bug Reports

This document contains **9 genuine bugs and anomalies** identified during the manual exploratory testing, mobile automation runs, and edge case evaluations of the **Kredily HRMS Android Mobile Application (`kredily-mobile-v2.apk`)** and backend services.

---

## 🐞 Bug Summary Matrix

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

---

## 📝 Detailed Defect Reports

### BUG-001: Attendance Correction Accepts Out Time Earlier Than In Time
- **Bug ID**: `BUG-001`
- **Severity**: **Medium**
- **Module**: Attendance → Regularization / Correction
- **Related Test Case**: [TC-003](TEST_CASES.md#tc-003--submit-attendance-correction-with-out-time-earlier-than-in-time)
- **Environment**: Kredily HRMS Mobile v2.0.0 on Android 11 (`emulator-5554`)

#### Steps to Reproduce:
1. Open Home screen and navigate to attendance anomaly.
2. Tap **Request correction**.
3. Set In time: `09:30 AM`.
4. Set Out time: `08:30 AM` (1 hour earlier than In time).
5. Enter a valid reason (e.g., "Shift correction").
6. Tap **Apply** / **Submit**.

#### Expected Result:
Same-day time sequences where Out time is chronologically earlier than In time must be rejected with a descriptive error (e.g., "Out time cannot be earlier than In time"). If overnight/graveyard shift is intended, the app must require explicit confirmation or multi-day date selection.

#### Actual Result:
The request was accepted without validation or warning. The system silently interpreted the earlier Out time as belonging to the next day, resulting in unintended 23-hour work duration calculations.

---

### BUG-002: Personal Email Validation Accepts Malformed Email Values
- **Bug ID**: `BUG-002`
- **Severity**: **Medium**
- **Module**: Profile → Edit Personal Information
- **Related Test Cases**: [TC-012](TEST_CASES.md#tc-012--save-malformed-personal-email), [TC-013](TEST_CASES.md#tc-013--save-personal-email-containing-an-internal-space)

#### Steps to Reproduce:
1. Navigate to **Profile** → **Edit Personal Information**.
2. In the **Personal Email** field, type `"abc"` (missing `@` and domain).
3. Tap **Save**.
4. Repeat the test with `"ab   c@gmail.com"` (space characters inside username).
5. Tap **Save**.

#### Expected Result:
Email validation regex must conform to RFC 5322. Both values must be blocked with an inline error: `"Please enter a valid email address"`.

#### Actual Result:
Both malformed values were successfully saved and persisted to the user profile without any client or backend validation errors.

#### Evidence & Context:
- **Screenshot**: `../screenshots/03_bug_002_bug_003_personal_info_validation.png`
- **Observed Value**: The saved Personal Information card explicitly displays `Personal email: ab   c@gmail.com`.

---

### BUG-003: Alternate Phone Field Accepts Invalid Numeric Lengths
- **Bug ID**: `BUG-003`
- **Severity**: **Low**
- **Module**: Profile → Edit Personal Information
- **Related Test Cases**: [TC-014](TEST_CASES.md#tc-014--save-9-digit-alternate-phone-number), [TC-015](TEST_CASES.md#tc-015--save-12-digit-alternate-phone-number)

#### Steps to Reproduce:
1. Navigate to **Profile** → **Edit Personal Information**.
2. Enter an invalid length number (e.g., 8 digits: `12345678` or 9 digits: `987654321`) in **Alternate Phone Number**.
3. Tap **Save**.

#### Expected Result:
System should enforce standard 10-digit mobile number validation (or E.164 standard with country code).

#### Actual Result:
The short number was accepted and persisted to the profile database without constraint.

#### Evidence & Context:
- **Screenshot**: `../screenshots/03_bug_002_bug_003_personal_info_validation.png`
- **Observed Value**: The saved Contact card explicitly displays `Alternate phone: 12345678`.

---

### BUG-004: Empty Education Record Can Be Created
- **Bug ID**: `BUG-004`
- **Severity**: **Medium**
- **Module**: Profile → Education
- **Related Test Case**: [TC-016](TEST_CASES.md#tc-016--save-education-record-with-all-required-fields-empty)

#### Steps to Reproduce:
1. Navigate to **Profile** → **Education**.
2. Tap **Add Education**.
3. Without entering degree, institution, or completion year, tap **Save**.

#### Expected Result:
Mandatory field validation should prevent submission and highlight missing fields.

#### Actual Result:
An empty education record row was generated and added to the employee profile.

---

### BUG-005: Future Family-Member Date of Birth (DOB) Is Accepted
- **Bug ID**: `BUG-005`
- **Severity**: **Low**
- **Module**: Profile → Family
- **Related Test Case**: [TC-017](TEST_CASES.md#tc-017--add-family-member-with-a-future-date-of-birth-dob)

#### Steps to Reproduce:
1. Navigate to **Profile** → **Family**.
2. Tap **Add Family Member**.
3. In Date of Birth field, pick a future date (e.g., `Jan 01, 2028` during September 2026 testing).
4. Tap **Save**.

#### Expected Result:
Date picker should disallow dates past today's date, or save action should reject future dates.

#### Actual Result:
Future DOB was accepted and saved to the family member profile without validation.

#### Evidence & Context:
- **Screenshot**: `../screenshots/02_bug_005_bug_006_family_emergency_contacts.png`
- **Observed Value**: Family member card displays: `"test person - Father · DOB Jan 01, 2028"`.

---

### BUG-006: Emergency Contact Phone Field Accepts Alphabetic & Invalid Short Values
- **Bug ID**: `BUG-006`
- **Severity**: **Medium**
- **Module**: Profile → Emergency Contacts
- **Related Test Case**: [TC-018](TEST_CASES.md#tc-018--save-emergency-contact-with-a-4-digit-phone-number)

#### Steps to Reproduce:
1. Navigate to **Profile** → **Family & Emergency Contacts**.
2. Tap **Add Emergency Contact**.
3. Enter name: `"test"`, Relation: `"Mother"`, Phone: `1234` (4 digits) → Tap **Save**.
4. Repeat with name: `"test"`, Relation: `"Son"`, Phone: `"ahcd"` (alphabetic string) → Tap **Save**.

#### Expected Result:
Phone input must enforce numeric keypad input and validate minimum 10 digits.

#### Actual Result:
Both `"1234"` and alphabetic `"ahcd"` were accepted and stored as emergency contact numbers.

#### Evidence & Context:
- **Screenshot**: `../screenshots/02_bug_005_bug_006_family_emergency_contacts.png`
- **Observed Values**: Emergency contacts list shows:
  - `"test · Mother · 1234"`
  - `"test · Son · ahcd"`

---

### BUG-007: Holiday Calendar Next-Month Navigation Is Unresponsive
- **Bug ID**: `BUG-007`
- **Severity**: **Low**
- **Module**: Profile → Holidays → Calendar
- **Status**: Exploratory Finding

#### Steps to Reproduce:
1. Open **Profile** → **Holidays**.
2. Switch to the **Calendar** tab (displaying current month, September 2026).
3. Tap on the right-arrow icon `>` to advance to the next month (October 2026).

#### Expected Result:
Calendar month transitions to October 2026 and displays upcoming company holidays.

#### Actual Result:
The next-month navigation arrow icon is completely unresponsive to tap events. The view remains locked to September 2026.

---

### BUG-008: Financial Leave-Year Option Is Unresponsive
- **Bug ID**: `BUG-008`
- **Severity**: **Medium**
- **Module**: Company Setup → Leave Setup
- **Status**: Exploratory Finding

#### Steps to Reproduce:
1. Navigate to **Company Setup** → **Leave Setup**.
2. Under Leave Year options, tap on **Financial (Apr–Mar)** radio/selector option.

#### Expected Result:
The Financial (Apr–Mar) option should become selected and adjust cycle calculations.

#### Actual Result:
The radio selection event did not trigger or update during testing; the option stayed unselected.

#### Evidence & Context:
- **Screenshot**: `../screenshots/04_company_setup_configuration.png`
- **Observed Value**: Leave Year remained locked to `"Calendar (Jan–Dec)"`.

---

### BUG-009: Attendance Correction Request Cannot Be Rejected ("Attendance log not found")
- **Bug ID**: `BUG-009`
- **Severity**: **High**
- **Module**: Approvals → Regularization (`Reg., 3`)
- **Related Test / Automation**: `AUTO-04` (`test_approval_rejection_workflow`)
- **Related Test Cases**: TC-006, TC-007, TC-008

#### Steps to Reproduce:
1. Navigate to **Approvals** → **Reg.** (Regularization requests).
2. Select pending attendance correction requests (e.g., 3 requests for Sep 22, 23, and 24).
3. Tap **Reject**.
4. In the decision modal (`decide-reason`), enter a valid rejection reason: `"Correction details could not be verified."`.
5. Tap the confirmation button (`decide-confirm`).

#### Expected Result:
Requests are successfully rejected. The status updates to `Rejected` and the items are cleared from the pending approval queue.

#### Actual Result:
App displays a prominent red banner:
> **`"3 couldn't be processed — Attendance log not found"`**
The rejection is aborted and the requests remain permanently stuck in pending state.

#### Evidence & Context:
- **Screenshot**: `../screenshots/05_bug_009_approvals_rejection_error.png`
- **Observed UI**: Rejection attempt triggered red error banner `"3 couldn't be processed — Attendance log not found"` with all 3 cards remaining selected in the queue.
