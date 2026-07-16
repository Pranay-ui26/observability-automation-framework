from pages.base_page import BasePage
from components.profile_menu import ProfileMenu
from locators.dashboard_locators import DashboardLocators


class DashboardPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.profile = ProfileMenu(page)

    # ==========================================================
    # Dashboard Page Verification
    # ==========================================================

    def verify_dashboard_is_loaded(self):
        self.verify_url_contains("overview")

        self.verify_element_is_visible(
            DashboardLocators.DASHBOARD_CONTAINER
        )

    def verify_dashboard_container(self):
        self.verify_element_is_visible(
            DashboardLocators.DASHBOARD_CONTAINER
        )

    # ==========================================================
    # Dashboard Widgets
    # ==========================================================

    def verify_topology_widget_is_displayed(self):
        self.verify_element_is_visible(
            DashboardLocators.TOPOLOGY_WIDGET
        )

    def verify_active_alerts_widget_is_displayed(self):
        self.verify_element_is_visible(
            DashboardLocators.ACTIVE_ALERTS_WIDGET
        )

    def verify_infrastructure_health_widget_is_displayed(self):
        self.verify_element_is_visible(
            DashboardLocators.INFRASTRUCTURE_HEALTH_WIDGET
        )

    def verify_ai_insights_widget_is_displayed(self):
        self.verify_element_is_visible(
            DashboardLocators.AI_INSIGHTS_WIDGET
        )

    # ==========================================================
    # Dashboard Actions
    # ==========================================================

    def refresh_dashboard(self):
        self.click_element(
            DashboardLocators.REFRESH_BUTTON
        )

        self.wait_for_network_to_be_idle()

    def verify_time_filter(self):
        self.verify_element_is_visible(
            DashboardLocators.TIME_RANGE_FILTER
        )