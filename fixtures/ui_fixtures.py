import time

import pytest
from config import settings as s
from ui.pages.home_page import HomePage
from ui.components.modals import CookieModal
from ui.pages.navigation import Navigation
from ui.web_driver import WebDriver


@pytest.fixture(scope='session')
def browser() -> WebDriver:
    a_browser = WebDriver().get_browser_instance(s.BROWSER)
    yield a_browser
    a_browser.quit()


@pytest.fixture(scope='module')
def home_page(browser: WebDriver()) -> HomePage:
    home_page = HomePage(browser)
    home_page.get('/')

    try:
        home_page.w.set_page_load_timeout(s.WEBDRIVER_ELEMENT_WAIT)
        cookie_modal = CookieModal(browser)
        home_page = cookie_modal.accept_all_cookies()
    except Exception as e:
        pass


    return home_page


@pytest.fixture(scope='module')
def site_navigation(browser: WebDriver()) -> Navigation:
    return Navigation(browser)