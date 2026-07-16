from config.config import BASE_URL, EMAIL_ADDRESS, PASSWORD
from playwright.sync_api import expect
from locators.login_locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def open_application(self):
        self.navigate_to_url(BASE_URL)

    def enter_email_address(self):
        self.logger.info(f"Email from .env: {EMAIL_ADDRESS}")
        print(f"Email from .env: {EMAIL_ADDRESS}")
        self.enter_text(LoginLocators.EMAIL, EMAIL_ADDRESS)

    def enter_password(self):
        self.enter_text(LoginLocators.PASSWORD, PASSWORD)

    def click_sign_in_button(self):
        self.logger.info("Clicking Sign In button")

        button = self.page.locator(LoginLocators.LOGIN_BUTTON)

        button.wait_for(state="visible")

        expect(button).to_be_enabled()

        print("Button Enabled:", button.is_enabled())

        button.click()

        print("Login button clicked")

    def login_to_application(self):
        self.open_application()

        self.enter_email_address()

        self.enter_password()

        self.click_sign_in_button()

        self.page.screenshot(path="login_result.png")

        self.page.wait_for_timeout(3000)

        print("Current URL:", self.page.url)
