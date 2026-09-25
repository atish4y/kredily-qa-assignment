from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class DashboardPage(BasePage):
    HEADER_TITLE = (AppiumBy.XPATH, "//*[contains(@text, 'Dashboard') or contains(@text, 'Welcome')]")
    CLOCK_IN_BTN = (AppiumBy.XPATH, "//*[@content-desc='clock_in_btn' or contains(@text, 'Clock In') or contains(@text, 'Punch In')]")
    WORK_DURATION = (AppiumBy.XPATH, "//*[@content-desc='work_duration' or contains(@text, 'Hrs')]")
    ATTENDANCE_TAB = (AppiumBy.XPATH, "//*[@content-desc='nav_attendance' or contains(@text, 'Attendance')]")
    LEAVE_TAB = (AppiumBy.XPATH, "//*[@content-desc='nav_leave' or contains(@text, 'Leave')]")
    PROFILE_TAB = (AppiumBy.XPATH, "//*[@content-desc='nav_profile' or contains(@text, 'Profile')]")

    def is_dashboard_displayed(self):
        element = self.find_element(self.HEADER_TITLE)
        return element is not None

    def get_work_duration(self):
        return self.get_text(self.WORK_DURATION)

    def navigate_to_attendance(self):
        return self.click(self.ATTENDANCE_TAB)

    def navigate_to_leave(self):
        return self.click(self.LEAVE_TAB)

    def navigate_to_profile(self):
        return self.click(self.PROFILE_TAB)
