import os

from config.constants import BrowserType

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


XMCY_URL = 'https://xm.com'
BROWSER = BrowserType.FIREFOX
BROWSER_HEADLESS = True # True|False
WEBDRIVER_ELEMENT_WAIT = 60
TESTS_OUTPUT_DIRECTORY = os.environ['TESTS_OUTPUT_DIRECTORY'] if 'TESTS_OUTPUT_DIRECTORY' in os.environ else PROJECT_ROOT

