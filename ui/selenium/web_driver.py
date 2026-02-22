from selenium import webdriver
from config.constants import BrowserType
from config import settings as s


class WebDriver:

    @staticmethod
    def get_browser_instance(browser_type):

        if browser_type == BrowserType.FIREFOX:
            browser_options = webdriver.FirefoxOptions()

        elif browser_type == BrowserType.CHROME:
            browser_options = webdriver.ChromeOptions()

        if s.BROWSER_HEADLESS:
            browser_options.add_argument("--headless=new")
            browser_options.add_argument("--no-sandbox")
            browser_options.add_argument("--disable-dev-shm-usage")
            browser_options.add_argument("--disable-gpu")
            browser_options.add_argument("--window-size=1920,1080")
            browser_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
            browser_options.add_argument("--disable-notifications")

        if browser_type == BrowserType.CHROME:
            # browser = webdriver.Chrome(options=browser_options, executable_path=ChromeDriverManager().install())
            browser = webdriver.Chrome(options=browser_options)

        elif BrowserType.FIREFOX:
            # browser = webdriver.Firefox(options=browser_options, executable_path=GeckoDriverManager().install())
            browser = webdriver.Firefox(options=browser_options)

        else:
            raise Exception("Browser was not defined")

        return browser
