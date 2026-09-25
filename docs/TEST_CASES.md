# Kredily HRMS Mobile Application - Functional Test Cases

This document details the **20 functional test cases** covering the major Human Resource Management System (HRMS) workflows on the **Kredily HRMS Android Mobile Application (`kredily-mobile-v2.apk`)**.

Test cases span **Positive**, **Negative**, and **Edge Cases** across core modules including Attendance, Approvals, Employee Directory, Profile Management, and Company Setup.

---

## 📊 Test Execution Summary

| Total Test Cases | Passed | Failed | Execution Environment | Execution Date |
| :---: | :---: | :---: | :---: | :---: |
| **20** | **13** | **7** | BlueStacks Android Emulator (Android 11 / x86_64, `emulator-5554`) | **25-09-2026** |

### Test Case Results Matrix

| Test Case ID | Workflow Module | Test Type | Result | Linked Defect |
| :--- | :--- | :--- | :---: | :--- |
| **TC-001** | Attendance / Requests | Positive | **PASS** | — |
| **TC-002** | Attendance / Correction | Negative | **PASS** | — |
| **TC-003** | Attendance / Correction | Negative / Edge | **FAIL** | **BUG-001** |
| **TC-004** | Home / Anomaly Navigation | Positive | **PASS** | — |
| **TC-005** | Attendance / Request Status | Positive | **PASS** | — |
| **TC-006** | Approvals / Rejection | Negative | **PASS** | — |
| **TC-007** | Approvals / Multi-Select | Edge | **PASS** | — |
| **TC-008** | Approvals / Bulk Actions | Positive | **PASS** | — |
| **TC-009** | Home / Employee Directory | Positive | **PASS** | — |
| **TC-010** | Employee Directory / Search | Positive | **PASS** | — |
| **TC-011** | Employee Directory / Search | Negative / Edge | **PASS** | — |
| **TC-012** | Profile / Personal Email | Negative | **FAIL** | **BUG-002** |
| **TC-013** | Profile / Personal Email | Negative | **FAIL** | **BUG-002** |
| **TC-014** | Profile / Alternate Phone | Edge | **FAIL** | **BUG-003** |
| **TC-015** | Profile / Alternate Phone | Edge | **FAIL** | **BUG-003** |
| **TC-016** | Profile / Education | Negative | **FAIL** | **BUG-004** |
| **TC-017** | Profile / Family Member | Edge | **FAIL** | **BUG-005** |
| **TC-018** | Profile / Emergency Contacts | Negative | **FAIL** | **BUG-006** |
| **TC-019** | Profile / Employee ID Card | Positive | **PASS** | — |
| **TC-020** | Company Setup / Invitations | Negative | **PASS** | — |

---

## 📋 Detailed Functional Test Cases

### TC-001 — Open an Existing Attendance Correction Request
- **Module**: Attendance → Requests
- **Type**: Positive
- **Preconditions**: User is logged into Kredily mobile app with prior attendance correction requests submitted.
- **Test Steps**:
  1. From Home screen, tap on **Attendance**.
  2. Navigate to the **Requests** tab.
  3. Locate and tap on an existing attendance correction request.
- **Expected Result**: Request details screen opens successfully showing the requested in/out times, reason, and status.
- **Actual Result**: Request details opened successfully without errors.
- **Result**: **PASS**

---

### TC-002 — Submit Attendance Correction with an Empty Reason
- **Module**: Attendance → Correction
- **Type**: Negative
- **Preconditions**: User has an attendance anomaly flagged on the Home or Attendance screen.
- **Test Steps**:
  1. Open attendance anomaly card.
  2. Tap **Request correction**.
  3. Enter valid In and Out times (e.g., In: 09:30 AM, Out: 06:30 PM).
  4. Leave the **Reason** text area completely empty.
  5. Tap **Apply** / **Submit**.
- **Expected Result**: Submission is blocked. Validation message indicates reason is mandatory.
- **Actual Result**: Submission was blocked until a valid reason was provided.
- **Result**: **PASS**

---

### TC-003 — Submit Attendance Correction with Out Time Earlier Than In Time
- **Module**: Attendance → Correction
- **Type**: Negative / Edge
- **Preconditions**: User initiates attendance correction request.
- **Test Steps**:
  1. Open attendance anomaly card and tap **Request correction**.
  2. Set In time: `09:30 AM`.
  3. Set Out time: `08:30 AM` (earlier than In time on the same date).
  4. Enter a valid reason (e.g., "Shift correction").
  5. Tap **Apply** / **Submit**.
- **Expected Result**: System rejects the invalid time sequence or explicitly requires the user to declare an overnight shift.
- **Actual Result**: Request accepted without warning; earlier Out time was implicitly interpreted as the next day.
- **Result**: **FAIL**
- **Linked Defect**: **BUG-001**

---

### TC-004 — Verify Home Fix Shortcut Navigates to Attendance Anomaly
- **Module**: Home Dashboard
- **Type**: Positive
- **Preconditions**: At least one attendance anomaly is present for the logged-in user.
- **Test Steps**:
  1. Launch Kredily app and land on **Home** dashboard.
  2. Locate the anomaly banner ("1 anomaly to fix").
  3. Tap the **Fix** shortcut button.
- **Expected Result**: App navigates directly to the relevant attendance anomaly detail view.
- **Actual Result**: Anomaly detail view opened immediately.
- **Result**: **PASS**

---

### TC-005 — Verify Attendance Correction Request Status After Submission
- **Module**: Attendance → Status
- **Type**: Positive
- **Preconditions**: Attendance correction request has just been submitted.
- **Test Steps**:
  1. Complete submission of attendance correction request.
  2. Navigate to Requests / Status view.
  3. Inspect the status badge of the newly submitted request.
- **Expected Result**: Status displays as `Submitted` / `Correction requested` / `Pending approval`.
- **Actual Result**: `Correction requested` status displayed correctly.
- **Result**: **PASS**

---

### TC-006 — Attempt to Reject Approval Request Without a Reason
- **Module**: Approvals → Regularization
- **Type**: Negative
- **Preconditions**: Logged-in user has manager/approver role with pending regularization requests.
- **Test Steps**:
  1. Tap **Approvals** from Home.
  2. Open **Reg.** (Regularization requests).
  3. Open a pending request and tap **Reject**.
  4. In the decision modal, leave the reason field empty and tap **Confirm Reject**.
- **Expected Result**: Rejection is blocked until a non-empty explanation is provided.
- **Actual Result**: Rejection reason was required; form could not be submitted empty.
- **Result**: **PASS**

---

### TC-007 — Select Multiple Approval Requests
- **Module**: Approvals → Bulk Actions
- **Type**: Edge
- **Preconditions**: Multiple regularization or leave requests are pending approval.
- **Test Steps**:
  1. Navigate to **Approvals** screen.
  2. Long-press or use multi-select checkboxes to select more than one pending item.
- **Expected Result**: Multiple requests can be checked/highlighted simultaneously.
- **Actual Result**: Multiple requests were selected successfully with active item counters.
- **Result**: **PASS**

---

### TC-008 — Verify Approve All / Reject Actions After Selection
- **Module**: Approvals → Bulk Actions
- **Type**: Positive
- **Preconditions**: At least one or more requests are selected via multi-select.
- **Test Steps**:
  1. Select one or more requests in the Approvals list.
  2. Verify the appearance of action buttons on the bottom/top toolbar.
- **Expected Result**: Contextual bulk actions (**Approve All**, **Reject**) appear clearly.
- **Actual Result**: Bulk **Approve All** and **Reject** buttons appeared as expected.
- **Result**: **PASS**

---

### TC-009 — Open Employee Directory
- **Module**: Home → Directory
- **Type**: Positive
- **Preconditions**: User is logged in on the Home screen.
- **Test Steps**:
  1. From Home screen, locate the **Directory** button.
  2. Tap **Directory**.
- **Expected Result**: Company Employee Directory opens, listing company members and search bar.
- **Actual Result**: Employee Directory opened smoothly.
- **Result**: **PASS**

---

### TC-010 — Search for an Existing Employee
- **Module**: Employee Directory
- **Type**: Positive
- **Preconditions**: Employee Directory is open; user "QA Assesment" exists in company tenant.
- **Test Steps**:
  1. In the Directory search bar (`dir-q`), type `"QA Assesment"`.
  2. Observe search result filter.
- **Expected Result**: Matching employee card appears in real-time or upon search execution.
- **Actual Result**: Employee card for "QA Assesment" appeared immediately.
- **Result**: **PASS**

---

### TC-011 — Search for a Nonexistent Employee
- **Module**: Employee Directory
- **Type**: Negative / Edge
- **Preconditions**: Employee Directory is open.
- **Test Steps**:
  1. In search input, enter a random nonexistent query: `"NonExistentUserXYZ_9999"`.
  2. Observe list behavior.
- **Expected Result**: No matching employee displayed; friendly empty state message shown.
- **Actual Result**: No matching employee displayed.
- **Result**: **PASS**

---

### TC-012 — Save Malformed Personal Email
- **Module**: Profile → Edit Personal Information
- **Type**: Negative
- **Preconditions**: User opens Profile → Edit Personal Information.
- **Test Steps**:
  1. Navigate to **Profile** → **Edit Personal Information**.
  2. Enter `"abc"` (missing `@` and domain) in the **Personal Email** field.
  3. Tap **Save**.
- **Expected Result**: Client-side or server-side email validation rejects the string with "Invalid email address".
- **Actual Result**: Malformed email value `"abc"` was accepted and persisted to profile.
- **Result**: **FAIL**
- **Linked Defect**: **BUG-002**

---

### TC-013 — Save Personal Email Containing an Internal Space
- **Module**: Profile → Edit Personal Information
- **Type**: Negative
- **Preconditions**: User opens Profile → Edit Personal Information.
- **Test Steps**:
  1. In **Personal Email** field, enter `"ab c@gmail.com"` (space within username part).
  2. Tap **Save**.
- **Expected Result**: Input rejected due to RFC 5322 compliance violation (spaces not allowed).
- **Actual Result**: Malformed email containing internal space was accepted and persisted.
- **Result**: **FAIL**
- **Linked Defect**: **BUG-002**

---

### TC-014 — Save 9-Digit Alternate Phone Number
- **Module**: Profile → Edit Personal Information
- **Type**: Edge
- **Preconditions**: User opens Profile → Edit Personal Information.
- **Test Steps**:
  1. Navigate to **Alternate Phone Number** field.
  2. Enter a 9-digit numeric string (e.g., `987654321`).
  3. Tap **Save**.
- **Expected Result**: Validation enforces standard 10-digit mobile number format.
- **Actual Result**: 9-digit alternate phone was accepted and persisted.
- **Result**: **FAIL**
- **Linked Defect**: **BUG-003**

---

### TC-015 — Save 12-Digit Alternate Phone Number
- **Module**: Profile → Edit Personal Information
- **Type**: Edge
- **Preconditions**: User opens Profile → Edit Personal Information.
- **Test Steps**:
  1. Navigate to **Alternate Phone Number** field.
  2. Enter a 12-digit numeric string without country code prefix (e.g., `987654321012`).
  3. Tap **Save**.
- **Expected Result**: Validation blocks numbers exceeding standard mobile length.
- **Actual Result**: 12-digit value was accepted and persisted.
- **Result**: **FAIL**
- **Linked Defect**: **BUG-003**

---

### TC-016 — Save Education Record with All Required Fields Empty
- **Module**: Profile → Education
- **Type**: Negative
- **Preconditions**: User navigates to Profile → Education section.
- **Test Steps**:
  1. Tap **Add Education**.
  2. Leave Degree, Institution, and Year of Passing blank.
  3. Tap **Save**.
- **Expected Result**: Form validation blocks submission and highlights required fields.
- **Actual Result**: Empty education record was created and saved to employee profile.
- **Result**: **FAIL**
- **Linked Defect**: **BUG-004**

---

### TC-017 — Add Family Member with a Future Date of Birth (DOB)
- **Module**: Profile → Family
- **Type**: Edge
- **Preconditions**: User navigates to Profile → Family Members.
- **Test Steps**:
  1. Tap **Add Family Member**.
  2. Enter member name and relation.
  3. Select a future Date of Birth (e.g., `Jan 1, 2028` tested on September 25, 2026).
  4. Tap **Save**.
- **Expected Result**: Future DOB is rejected with "Date of birth cannot be in the future".
- **Actual Result**: Future DOB was accepted and saved without warning.
- **Result**: **FAIL**
- **Linked Defect**: **BUG-005**

---

### TC-018 — Save Emergency Contact with a 4-Digit Phone Number
- **Module**: Profile → Emergency Contacts
- **Type**: Negative
- **Preconditions**: User navigates to Profile → Emergency Contacts.
- **Test Steps**:
  1. Tap **Add Emergency Contact**.
  2. Enter Name: "Emergency Test".
  3. Enter Phone: `1234` (or alphabetic `"ahcd"`).
  4. Tap **Save**.
- **Expected Result**: Input validation rejects invalid phone numbers.
- **Actual Result**: 4-digit number and alphabetic characters were accepted and saved.
- **Result**: **FAIL**
- **Linked Defect**: **BUG-006**

---

### TC-019 — Open Employee ID Card
- **Module**: Profile → ID Card
- **Type**: Positive
- **Preconditions**: User is logged in.
- **Test Steps**:
  1. Navigate to **Profile** tab.
  2. Tap on **ID Card**.
- **Expected Result**: Digital Employee ID card opens showing photo, employee code, name, and designation.
- **Actual Result**: ID card opened cleanly with all employee details displayed.
- **Result**: **PASS**

---

### TC-020 — Attempt Employee Invitation Using an Invalid 4-Digit Mobile Number
- **Module**: Company Setup → Employee Invitation
- **Type**: Negative
- **Preconditions**: Admin user navigates to Company Setup / Invitations.
- **Test Steps**:
  1. Open Company Setup → Employee Invitation.
  2. Enter candidate Name.
  3. Enter 4-digit mobile number: `9876`.
  4. Tap **Invite**.
- **Expected Result**: Invalid mobile format is rejected.
- **Actual Result**: Invitation was rejected with error message: `"Phone number is not valid."`
- **Result**: **PASS**
