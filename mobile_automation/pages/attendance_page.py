from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class AttendancePage(BasePage):
    PUNCH_BUTTON = (AppiumBy.XPATH, "//*[@content-desc='punch_button' or contains(@text, 'CLOCK IN') or contains(@text, 'CLOCK OUT')]")
    PUNCH_STATUS_MSG = (AppiumBy.XPATH, "//*[contains(@text, 'allowed to do punch') or contains(@text, 'Punch Status')]")
    REGULARIZE_BTN = (AppiumBy.XPATH, "//*[contains(@text, 'Regularize')]")
    ATTENDANCE_LOG_HEADER = (AppiumBy.XPATH, "//*[contains(@text, 'Attendance Log')]")

    def click_punch(self):
        return self.click(self.PUNCH_BUTTON)

    def get_punch_status_message(self):
        return self.get_text(self.PUNCH_STATUS_MSG)

    def is_attendance_log_visible(self):
        return self.find_element(self.ATTENDANCE_LOG_HEADER) is not None
