from pages.base_page import BasePage
from components.profile_menu import ProfileMenu


class DashboardPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.profile = ProfileMenu(page)

    def verify_dashboard_is_loaded(self):
        self.verify_url_contains("overview")
        self.verify_element_is_visible("main")

    def verify_widget_is_displayed(self, locator):
        self.verify_element_is_visible(locator)

    def verify_widgets_are_displayed(self, widgets):
        for widget in widgets:
            self.verify_element_is_visible(widget)

    def verify_time_filter(self, locator):
        self.verify_element_is_visible(locator)

    def verify_refresh_button(self, locator):
        self.verify_element_is_visible(locator)

    def refresh_dashboard(self, locator):
        self.click_element(locator)
        self.wait_for_network_to_be_idle()