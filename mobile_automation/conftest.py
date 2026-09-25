import pytest
import os
import requests
from utils.driver_factory import DriverFactory

@pytest.fixture(scope="session")
def app_path():
    possible_path = os.path.abspath("kredily-mobile-v2.apk")
    if os.path.exists(possible_path):
        return possible_path
    parent_path = os.path.abspath("../kredily-mobile-v2.apk")
    if os.path.exists(parent_path):
        return parent_path
    return None

@pytest.fixture(scope="function")
def driver(app_path):
    driver_instance = DriverFactory.get_driver(app_path=app_path)
    yield driver_instance
    if driver_instance:
        try:
            driver_instance.quit()
        except Exception:
            pass

@pytest.fixture(scope="session")
def api_auth_session():
    """Provides an authenticated session for API verification fallbacks."""
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Mobile)",
        "Content-Type": "application/json",
        "Accept": "application/json"
    })
    
    login_url = "https://app.upgrade.kredily.com/ws/v1/accounts/set-password-login/"
    payload = {
        "email": "peoplekredily1@yopmail.com",
        "password": "Pass@9865"
    }
    res = session.post(login_url, json=payload, timeout=10)
    if res.status_code == 200:
        data = res.json()
        token = data.get("token")
        if token:
            session.headers.update({"Authorization": f"Token {token}"})
    return session
