import requests
import json
import sys

BASE_URL = "https://app.upgrade.kredily.com"
EMAIL = "peoplekredily1@yopmail.com"
PASS = "Pass@9865"

def run_api_suite():
    print("\n=======================================================")
    print("      KREDILY HRMS API AUTOMATION TEST SUITE RUNNER    ")
    print("=======================================================")
    
    passed = 0
    failed = 0

    # 1. Login API Positive
    print("\n[TEST 1] POST /ws/v1/accounts/set-password-login/ (Valid Credentials)")
    res = requests.post(f"{BASE_URL}/ws/v1/accounts/set-password-login/", json={"email": EMAIL, "password": PASS}, timeout=10)
    if res.status_code == 200 and "token" in res.json():
        token = res.json()["token"]
        print(f" -> PASS (200 OK). Token acquired: {token[:12]}...")
        passed += 1
    else:
        print(f" -> FAIL ({res.status_code}): {res.text[:100]}")
        failed += 1
        sys.exit(1)

    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}

    # 2. Login API Negative
    print("\n[TEST 2] POST /ws/v1/accounts/set-password-login/ (Invalid User)")
    res_neg = requests.post(f"{BASE_URL}/ws/v1/accounts/set-password-login/", json={"email": "nonexistent_999@yopmail.com", "password": PASS}, timeout=10)
    if res_neg.status_code == 400 and "Please contact support@kredily.com" in res_neg.json().get("message", ""):
        print(" -> PASS (400 Bad Request correctly returned).")
        passed += 1
    else:
        print(f" -> FAIL ({res_neg.status_code}): {res_neg.text[:100]}")
        failed += 1

    # 3. Dashboard API Positive
    print("\n[TEST 3] GET /ws/v2/company/dashboard/ (Authenticated Dashboard Status)")
    res = requests.get(f"{BASE_URL}/ws/v2/company/dashboard/", headers=headers, timeout=10)
    if res.status_code == 200 and "punch_validations" in res.json().get("data", {}):
        print(" -> PASS (200 OK). Punch validations retrieved.")
        passed += 1
    else:
        print(f" -> FAIL ({res.status_code}): {res.text[:100]}")
        failed += 1

    # 4. Leave Balances API Positive
    print("\n[TEST 4] GET /mapi/v1/leave/balances/me/ (User Leave Balances)")
    res = requests.get(f"{BASE_URL}/mapi/v1/leave/balances/me/", headers=headers, timeout=10)
    if res.status_code == 200:
        by_type = res.json().get("data", {}).get("by_type", [])
        casual = next((l for l in by_type if l.get("leave_type_label") == "Casual Leave"), {})
        print(f" -> PASS (200 OK). Casual Leave Balance: {casual.get('balance')} days.")
        passed += 1
    else:
        print(f" -> FAIL ({res.status_code}): {res.text[:100]}")
        failed += 1

    # 5. Unauthorized Access Negative
    print("\n[TEST 5] GET /ws/v2/company/dashboard/ (Unauthenticated - No Token)")
    res = requests.get(f"{BASE_URL}/ws/v2/company/dashboard/", timeout=10)
    if res.status_code in [401, 403]:
        print(f" -> PASS ({res.status_code} Access Denied correctly enforced).")
        passed += 1
    else:
        print(f" -> FAIL ({res.status_code}): Expected 401 or 403")
        failed += 1

    # 6. BUG-01 Verification
    print("\n[TEST 6] GET /mapi/v1/livetrack/my/plans/ (BUG-01: 503 SCHEMA_PENDING)")
    res = requests.get(f"{BASE_URL}/mapi/v1/livetrack/my/plans/", headers=headers, timeout=10)
    if res.status_code == 503 and res.json().get("error", {}).get("code") == "SCHEMA_PENDING":
        print(" -> PASS (503 Service Unavailable BUG-01 verified).")
        passed += 1
    else:
        print(f" -> FAIL ({res.status_code}): {res.text[:100]}")
        failed += 1

    # 7. BUG-02 Verification
    print("\n[TEST 7] GET /kapi/v1/payroll/core/payslip/ (BUG-02: Payslip Raw HTML Response)")
    res = requests.get(f"{BASE_URL}/kapi/v1/payroll/core/payslip/", headers=headers, timeout=10)
    if res.status_code == 200 and "text/html" in res.headers.get("Content-Type", ""):
        print(" -> PASS (Raw HTML bug response verified).")
        passed += 1
    else:
        print(f" -> FAIL ({res.status_code}): {res.text[:100]}")
        failed += 1

    print("\n=======================================================")
    print(f"   API TEST SUITE SUMMARY: {passed} PASSED, {failed} FAILED   ")
    print("=======================================================\n")

if __name__ == "__main__":
    run_api_suite()
