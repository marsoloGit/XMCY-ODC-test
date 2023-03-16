import pytest
from config import settings as s
from ui.playwright.components.modals import CookieModal
from ui.playwright.pages.home_page import HomePage
from playwright.sync_api import Playwright


@pytest.fixture(scope='session')
def browser(playwright: Playwright):
    browser = getattr(playwright, s.BROWSER.value).launch(headless=False)

    yield browser
    browser.close()


@pytest.fixture(scope='module')
def page(browser, playwright: Playwright):
    context = browser.new_context(
        base_url=s.XMCY_URL,
        viewport={
            "width": 1920,
            "height": 1080,
        }
    )
    page = context.new_page()
    yield page
    page.close


@pytest.fixture(scope='module')
def home_page(page):
    page.goto('/')
    try:
        CookieModal(page).accept_all_cookies()
    except Exception:
        pass

    return HomePage(page)


# @pytest.fixture
# def page(browser, playwright: Playwright):
#     iphone_11 = playwright.devices['iPhone 11 Pro']
#     context = browser.new_context(
#         base_url='https://playwright.dev',
#         geolocation={'latitude': 51.508076,'longitude': -0.0993827,},
#         permissions= ['geolocation'],
#         **iphone_11,
#     )
#     return context.new_page()
