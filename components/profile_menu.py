from pages.base_page import BasePage
from locators.dashboard_locators import DashboardLocators
from locators.login_locators import LoginLocators


class ProfileMenu(BasePage):

    def open_profile_menu(self):
        self.click_element(DashboardLocators.PROFILE_ICON)

    def click_sign_out(self):
        self.click_element(DashboardLocators.SIGN_OUT_BUTTON)

    def logout(self):
        self.open_profile_menu()

        self.click_sign_out()

        self.wait_for_network_to_be_idle()

        self.verify_element_is_visible(LoginLocators.LOGIN_BUTTON)