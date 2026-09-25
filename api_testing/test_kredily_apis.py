import pytest
import requests

BASE_URL = "https://app.upgrade.kredily.com"
VALID_EMAIL = "peoplekredily1@yopmail.com"
VALID_PASS = "Pass@9865"

@pytest.fixture(scope="session")
def auth_token():
    url = f"{BASE_URL}/ws/v1/accounts/set-password-login/"
    payload = {"email": VALID_EMAIL, "password": VALID_PASS}
    res = requests.post(url, json=payload, timeout=10)
    assert res.status_code == 200, f"Auth failed with status {res.status_code}"
    token = res.json().get("token")
    assert token is not None, "Token missing from response"
    return token

@pytest.fixture(scope="session")
def auth_headers(auth_token):
    return {
        "Authorization": f"Token {auth_token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

# -------------------------------------------------------------
# POSITIVE SCENARIOS
# -------------------------------------------------------------

def test_api_login_positive():
    """Positive API Test: Valid credentials login returns token and user info."""
    url = f"{BASE_URL}/ws/v1/accounts/set-password-login/"
    payload = {"email": VALID_EMAIL, "password": VALID_PASS}
    res = requests.post(url, json=payload, timeout=10)
    assert res.status_code == 200
    data = res.json()
    assert "token" in data
    assert data.get("email") == VALID_EMAIL

def test_api_dashboard_positive(auth_headers):
    """Positive API Test: Dashboard metrics returns punch validations and rules."""
    url = f"{BASE_URL}/ws/v2/company/dashboard/"
    res = requests.get(url, headers=auth_headers, timeout=10)
    assert res.status_code == 200
    data = res.json().get("data", {})
    assert "punch_validations" in data

def test_api_leave_balances_positive(auth_headers):
    """Positive API Test: Leave balances returns Casual Leave balance > 0."""
    url = f"{BASE_URL}/mapi/v1/leave/balances/me/"
    res = requests.get(url, headers=auth_headers, timeout=10)
    assert res.status_code == 200
    types = res.json().get("data", {}).get("by_type", [])
    casual = next((l for l in types if l.get("leave_type_label") == "Casual Leave"), None)
    assert casual is not None
    assert float(casual.get("balance")) > 0

def test_api_capabilities_positive(auth_headers):
    """Positive API Test: Capabilities API returns module permissions."""
    url = f"{BASE_URL}/mapi/v1/capabilities/"
    res = requests.get(url, headers=auth_headers, timeout=10)
    assert res.status_code == 200
    data = res.json().get("data", {})
    assert data.get("modules", {}).get("attendance") is True

# -------------------------------------------------------------
# NEGATIVE & EDGE-CASE SCENARIOS
# -------------------------------------------------------------

def test_api_login_invalid_password_negative():
    """Negative API Test: Invalid password login attempt rejected."""
    url = f"{BASE_URL}/ws/v1/accounts/set-password-login/"
    payload = {"email": VALID_EMAIL, "password": "WrongPassword123"}
    res = requests.post(url, json=payload, timeout=10)
    assert res.status_code in [200, 400, 401]
    assert "token" not in res.json()

def test_api_unauthorized_access_negative():
    """Negative API Test: Accessing protected endpoint without token returns 401."""
    url = f"{BASE_URL}/ws/v2/company/dashboard/"
    res = requests.get(url, headers={}, timeout=10)
    assert res.status_code == 401

def test_api_bug_01_livetrack_503_negative(auth_headers):
    """Bug Scenario API Test (BUG-01): Meeting plans endpoint returns 503 SCHEMA_PENDING."""
    url = f"{BASE_URL}/mapi/v1/livetrack/my/plans/"
    res = requests.get(url, headers=auth_headers, timeout=10)
    assert res.status_code == 503
    assert res.json().get("error", {}).get("code") == "SCHEMA_PENDING"

def test_api_bug_02_payslip_raw_html_negative(auth_headers):
    """Bug Scenario API Test (BUG-02): Payslip API returns HTML content instead of JSON."""
    url = f"{BASE_URL}/kapi/v1/payroll/core/payslip/"
    res = requests.get(url, headers=auth_headers, timeout=10)
    assert res.status_code == 200
    assert "text/html" in res.headers.get("Content-Type", "")
    assert "<!doctype html>" in res.text.lower()
