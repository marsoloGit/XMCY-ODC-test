import pytest
from config import settings as s
from ui.playwright.components.modals import CookieModal
from ui.playwright.pages.home_page import HomePage
from ui.playwright.pages.all_in_one_calculator_page import AllInOneCalculatorPage
from ui.playwright.pages.currency_calculator_page import CurrencyCalculatorPage
from playwright.sync_api import Playwright


@pytest.fixture(scope='session')
def browser_pw(playwright: Playwright):
    # 'chrome' channel uses the actual Google Chrome browser instead of Chromium
    # which is much harder for anti-bot systems to detect.
    browser = getattr(playwright, s.BROWSER.value).launch(
        headless=s.BROWSER_HEADLESS,
        channel="chrome",
        args=[
            "--disable-blink-features=AutomationControlled",
        ]
    )

    yield browser
    browser.close()
s

@pytest.fixture(scope='module')
def page(browser_pw, playwright: Playwright):
    context = browser_pw.new_context(
        base_url=s.XMCY_URL,
        viewport={
            "width": 1920,
            "height": 1080,
        },
        user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        extra_http_headers={
            "Accept-Language": "en-US,en;q=0.9",
        },
        bypass_csp=True,
        ignore_https_errors=True,
    )
    page = context.new_page()
    # Increase default navigation timeout
    page.set_default_navigation_timeout(60000)
    page.set_default_timeout(60000)
    yield page
    page.close()



@pytest.fixture(scope='module')
def home_page_pw(page):
    # Use domcontentloaded to be faster but still have the DOM ready
    # Sometimes 'load' event never fires due to tracking scripts
    page.goto('/', wait_until='domcontentloaded')

    # Give the cookie modal some time to appear, but don't fail if it doesn't
    try:
        cookie_modal = CookieModal(page)
        cookie_modal.modal_container.wait_for(state='visible', timeout=10000)
        cookie_modal.accept_all_cookies()
    except Exception:
        pass

    return HomePage(page)



@pytest.fixture(scope='module')
def all_in_one_calc_page(page):
    return AllInOneCalculatorPage(page)


@pytest.fixture(scope='module')
def currency_calc_page(page):
    return CurrencyCalculatorPage(page)


@pytest.fixture(scope='session')
def storage_state(browser_pw):
    # Create a temporary context to get the cookie consent
    context = browser_pw.new_context(
        viewport={"width": 1920, "height": 1080},
    )
    page = context.new_page()
    page.goto(s.XMCY_URL)

    # Handle cookie modal
    try:
        cookie_modal = CookieModal(a_page)
        cookie_modal.modal_container.wait_for(state='visible', timeout=10000)
        cookie_modal.modal_container.wait_for(state='visible', timeout=10000)
        cookie_modal.accept_all_cookies()
        # Wait a bit for the cookie to be saved
        page.wait_for_timeout(1000)
    except Exception:
        pass

    # Save storage state into a file
    context.storage_state(path=s.STORAGE_STATE_PATH)
    context.close()
    return s.STORAGE_STATE_PATH

#
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
