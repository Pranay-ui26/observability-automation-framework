from playwright.sync_api import expect
from utilities.logger import Logger


class BasePage:
    """
    BasePage contains all reusable browser actions.
    Every Page Object should inherit from this class.
    """

    def __init__(self, page):
        self.page = page
        self.logger = Logger.get_logger(self.__class__.__name__)

    # ==========================================================
    # Navigation Methods
    # ==========================================================

    def navigate_to_url(self, url):
        self.logger.info(f"Navigating to URL: {url}")
        self.page.goto(url)

    def refresh_current_page(self):
        self.logger.info("Refreshing current page")
        self.page.reload()

    def get_current_url(self):
        return self.page.url

    def verify_url_contains(self, expected_text):
        actual_url = self.page.url
        assert expected_text in actual_url, \
            f"Expected URL to contain '{expected_text}', but found '{actual_url}'"

    # ==========================================================
    # Element Interaction Methods
    # ==========================================================

    def click_element(self, locator):
        self.logger.info(f"Clicking element: {locator}")

        element = self.page.locator(locator)

        element.wait_for(state="visible")

        expect(element).to_be_enabled()

        element.click()

    def enter_text(self, locator, value):
        element = self.page.locator(locator)

        element.wait_for(state="visible")

        print("Before:", element.input_value())

        element.fill(value)

        print("After:", element.input_value())

    def clear_text(self, locator):
        self.logger.info(f"Clearing text from: {locator}")

        element = self.page.locator(locator)

        element.click()

        element.press("Control+A")

        element.press("Delete")

    def hover_over_element(self, locator):
        self.logger.info(f"Hovering over: {locator}")

        self.page.locator(locator).hover()

    def double_click_element(self, locator):
        self.logger.info(f"Double clicking: {locator}")

        self.page.locator(locator).dblclick()

    def right_click_element(self, locator):
        self.logger.info(f"Right clicking: {locator}")

        self.page.locator(locator).click(button="right")

    # ==========================================================
    # Verification Methods
    # ==========================================================

    def verify_element_is_visible(self, locator):
        self.logger.info(f"Verifying visibility of: {locator}")

        expect(self.page.locator(locator)).to_be_visible()

    def verify_element_is_hidden(self, locator):
        self.logger.info(f"Verifying element is hidden: {locator}")

        expect(self.page.locator(locator)).to_be_hidden()

    def is_element_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def is_element_enabled(self, locator):
        return self.page.locator(locator).is_enabled()

    # ==========================================================
    # Get Data Methods
    # ==========================================================

    def get_element_text(self, locator):
        return self.page.locator(locator).inner_text()

    def get_input_field_value(self, locator):
        return self.page.locator(locator).input_value()

    # ==========================================================
    # Keyboard Actions
    # ==========================================================

    def press_keyboard_key(self, key):
        self.logger.info(f"Pressing keyboard key: {key}")

        self.page.keyboard.press(key)

    # ==========================================================
    # Wait Methods
    # ==========================================================

    def wait_for_page_to_load(self):
        self.logger.info("Waiting for page load")

        self.page.wait_for_load_state("load")

    def wait_for_network_to_be_idle(self):
        self.logger.info("Waiting for network to become idle")

        self.page.wait_for_load_state("networkidle")

    def wait_for_dom_content_loaded(self):
        self.logger.info("Waiting for DOM content to load")

        self.page.wait_for_load_state("domcontentloaded")

    # ==========================================================
    # Scroll Methods
    # ==========================================================

    def scroll_to_element(self, locator):
        self.logger.info(f"Scrolling to: {locator}")

        self.page.locator(locator).scroll_into_view_if_needed()

    # ==========================================================
    # Screenshot Methods
    # ==========================================================

    def capture_screenshot(self, file_name):
        self.logger.info(f"Capturing screenshot: {file_name}")

        self.page.screenshot(path=f"screenshots/{file_name}")