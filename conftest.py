import pytest
from playwright.sync_api import sync_playwright
from config.config import *
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@pytest.fixture(scope="session")
def browser():

    with sync_playwright() as p:

        if BROWSER == "chromium":

            browser = p.chromium.launch(
                headless=HEADLESS,
                slow_mo=SLOW_MO
            )

        elif BROWSER == "firefox":

            browser = p.firefox.launch(
                headless=HEADLESS
            )

        else:

            browser = p.webkit.launch(
                headless=HEADLESS
            )

        yield browser

        browser.close()


@pytest.fixture()
def page(browser):

    context = browser.new_context()

    page = context.new_page()

    page.set_default_timeout(TIMEOUT)

    yield page

    context.close()


@pytest.fixture()
def login(page):
    return LoginPage(page)


@pytest.fixture()
def dashboard_page(page):
    return DashboardPage(page)


@pytest.fixture
def authenticated_session(login):
    login.login_to_application()
    return login