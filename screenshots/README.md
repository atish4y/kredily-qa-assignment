# Test Evidence & Screenshots Catalog

This directory contains real mobile application screenshots captured from live testing sessions on the BlueStacks Android emulator (`emulator-5554`) running the **Kredily HRMS Android APK (`kredily-mobile-v2.apk`)**.

---

## 📸 Screenshots & Context

### 1. `01_dashboard_live_screen.png`
- **Associated Workflow / Tests**: `AUTO-02`, `TC-004`, Home Dashboard Navigation
- **Module**: Home Dashboard & Live Clock-in
- **Context & Verification**:
  - Displays the live authenticated dashboard for logged-in user **QA Assesment**.
  - Confirms shift tracking status (`12:51:19 Clocked In`, Shift: 9:30 AM – 6:30 PM).
  - Displays real-time pending approvals banner: `"Needs you: 3 approvals waiting (0 leave · 3 corrections)"` with direct navigation shortcut.
  - Highlights team attendance counters (`1 In`, `0 Late`, `0 Leave`, `0 Absent`) and weekly attendance timeline.
  - Confirms visibility and active selection of the bottom **Home** navigation tab used in `AUTO-02`.

---

### 2. `02_bug_005_bug_006_family_emergency_contacts.png`
- **Associated Defects**: `BUG-005`, `BUG-006`
- **Associated Test Cases**: `TC-017`, `TC-018`
- **Module**: Profile → Family Members & Emergency Contacts
- **Context & Defect Observations**:
  - **BUG-005 Evidence**: Under **Family members**, the record for `"test person"` (Father) was saved with a future Date of Birth: **`DOB Jan 01, 2028`** (tested in September 2026). The system permitted saving a future birthdate without validation.
  - **BUG-006 Evidence**: Under **Emergency contacts**, two critical validation bypasses are shown:
    1. Contact `"test"` (Mother) saved with an invalid 4-digit number: **`1234`**.
    2. Contact `"test"` (Son) saved with purely alphabetic string as phone number: **`ahcd`**.

---

### 3. `03_bug_002_bug_003_personal_info_validation.png`
- **Associated Defects**: `BUG-002`, `BUG-003`
- **Associated Test Cases**: `TC-012`, `TC-013`, `TC-014`, `TC-015`
- **Module**: Profile → Personal Information
- **Context & Defect Observations**:
  - **BUG-002 Evidence**: The **Personal email** field accepted and persisted the malformed value **`ab   c@gmail.com`** (containing internal whitespace between username characters), violating RFC 5322 email syntax rules.
  - **BUG-003 Evidence**: The **Alternate phone** field accepted and persisted an invalid 8-digit value **`12345678`**, failing to enforce standard 10-digit mobile number formatting.

---

### 4. `04_company_setup_configuration.png`
- **Associated Workflow / Tests**: `TC-020`, `BUG-008`, Company Onboarding
- **Module**: Company Setup → Configuration Summary
- **Context & Verification**:
  - Displays the post-configuration summary screen ("All set! Your company is ready.").
  - Outlines company-wide defaults: Shift timing (09:30 AM – 06:30 PM with 10 min grace), GPS attendance toggles, geofencing, selfie verification, and Leave Year cycle (**Calendar Jan–Dec**).
  - Used during exploratory evaluation of Company Setup and Leave Year configuration options (`BUG-008`).

---

### 5. `05_bug_009_approvals_rejection_error.png`
- **Associated Defect**: `BUG-009`
- **Associated Automation**: `AUTO-04` (`test_approval_rejection_workflow`)
- **Associated Test Cases**: `TC-006`, `TC-007`, `TC-008`
- **Module**: Approvals → Regularization (`Reg., 3`)
- **Context & Defect Observations**:
  - Highlights 3 selected regularization requests submitted by **QA Assesment** for Sep 22, Sep 23, and Sep 24.
  - Demonstrates multi-select capability (`3 selected`, `Approve all`, `Reject`).
  - **Critical Failure**: When attempting to process or reject the selected requests, the backend application fails with a prominent red error message:
    > **`"3 couldn't be processed — Attendance log not found"`**
  - Confirms defect **BUG-009** identified during manual exploratory testing and captured dynamically during automated test execution of `AUTO-04`.
