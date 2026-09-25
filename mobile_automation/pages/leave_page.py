from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class LeavePage(BasePage):
    CASUAL_LEAVE_BALANCE = (AppiumBy.XPATH, "//*[contains(@text, 'Casual Leave')]/following-sibling::*[contains(@text, '13.5') or contains(@text, 'Balance')]")
    APPLY_LEAVE_BTN = (AppiumBy.XPATH, "//*[@content-desc='apply_leave_btn' or contains(@text, 'Apply Leave')]")
    LEAVE_TYPE_DROPDOWN = (AppiumBy.XPATH, "//*[@content-desc='leave_type_select' or contains(@text, 'Select Leave Type')]")
    REASON_INPUT = (AppiumBy.XPATH, "//android.widget.EditText[contains(@text, 'Reason')]")
    SUBMIT_LEAVE_BTN = (AppiumBy.XPATH, "//*[@content-desc='submit_leave' or contains(@text, 'Submit')]")
    SUCCESS_TOAST = (AppiumBy.XPATH, "//*[contains(@text, 'submitted successfully')]")

    def get_casual_leave_balance(self):
        return self.get_text(self.CASUAL_LEAVE_BALANCE)

    def click_apply_leave(self):
        return self.click(self.APPLY_LEAVE_BTN)

    def fill_leave_form(self, reason):
        self.send_keys(self.REASON_INPUT, reason)
        return self.click(self.SUBMIT_LEAVE_BTN)
