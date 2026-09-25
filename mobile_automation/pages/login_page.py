from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL_INPUT = (AppiumBy.XPATH, "//android.widget.EditText[@content-desc='email_input' or contains(@text, 'Email')]")
    PASSWORD_INPUT = (AppiumBy.XPATH, "//android.widget.EditText[@content-desc='password_input' or contains(@text, 'Password')]")
    LOGIN_BUTTON = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='login_button' or contains(@text, 'LOGIN') or contains(@text, 'Sign In')]")
    ERROR_MESSAGE = (AppiumBy.XPATH, "//*[@content-desc='error_msg' or contains(@text, 'invalid') or contains(@text, 'contact support')]")
    FORGOT_PASSWORD_LINK = (AppiumBy.XPATH, "//*[contains(@text, 'Forgot Password')]")

    def enter_email(self, email):
        return self.send_keys(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        return self.send_keys(self.PASSWORD_INPUT, password)

    def click_login(self):
        return self.click(self.LOGIN_BUTTON)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
