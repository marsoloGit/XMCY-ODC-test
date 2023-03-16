from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from config.constants import BrowserType


class WebDriver:

    @staticmethod
    def get_browser_instance(browser_type):

        if browser_type == BrowserType.FIREFOX:
            browser_options = webdriver.FirefoxOptions()

        elif browser_type == BrowserType.CHROME:
            browser_options = webdriver.ChromeOptions()

        # browser_options.add_argument("--headless")
        # browser_options.add_argument("--no-sandbox")
        # browser_options.add_argument("--disable-dev-shm-usage")
        # browser_options.add_argument("--disable-gpu")
        # browser_options.add_argument("--start-maximized")
        # browser_options.add_argument('window-size=1920,1080')

        if browser_type == BrowserType.CHROME:
            browser = webdriver.Chrome(options=browser_options, executable_path=ChromeDriverManager().install())
        elif BrowserType.FIREFOX:
            browser = webdriver.Firefox(options=browser_options, executable_path=GeckoDriverManager().install())

        else:
            raise Exception("Browser was not defined")

        return browser
