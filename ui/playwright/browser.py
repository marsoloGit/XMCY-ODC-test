from config.constants import BrowserType
from playwright.sync_api import sync_playwright


def get_browser_instance(browser_type):
    with sync_playwright() as p:
        if browser_type == BrowserType.CHROME.value:
            browser = p.chromium.launch(headless=False)
        elif browser_type == BrowserType.FIREFOX.value:
            browser = p.firefox.launch(headless=False)
        else:
            raise Exception("Browser was not defined")
        page = browser.new_page()
    return page
