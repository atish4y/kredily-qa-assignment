import os
from appium import webdriver
from appium.options.android import UiAutomator2Options

class DriverFactory:
    @staticmethod
    def get_driver(app_path=None, device_name="Android Emulator", platform_version="11.0", appium_url="http://localhost:4723"):
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.device_name = device_name
        options.platform_version = platform_version
        options.automation_name = "UiAutomator2"
        options.app_package = "com.kredily.mobile"
        options.app_activity = "com.kredily.mobile.MainActivity"
        options.no_reset = False
        options.auto_grant_permissions = True
        
        if app_path and os.path.exists(app_path):
            options.app = os.path.abspath(app_path)
            
        try:
            driver = webdriver.Remote(command_executor=appium_url, options=options)
            driver.implicitly_wait(10)
            return driver
        except Exception as e:
            print(f"[DriverFactory] Note: Appium server not active or local emulator offline: {e}")
            return None
