import os
from page_objects import PageObject
from retry import retry
from config import settings as s
from tools.utils import unique_time_stamp

ELEMENT_TIMEOUT = s.WEBDRIVER_ELEMENT_WAIT


class BasePage(PageObject):
    def __init__(self, webdriver, root_uri=s.XMCY_URL):
        super(BasePage, self).__init__(webdriver, root_uri)

    page_url = None
    page_name = None


    def get_without_root_uri(self, uri):
        """
        :param uri:  root_uri attribute is '' here.
        """
        self.w.get(uri)


    @retry(Exception, tries=3, delay=1)
    def is_present(self, webelement):
        return webelement is not None and webelement != []



    def save_screenshot(self, output_dir: str = s.TESTS_OUTPUT_DIRECTORY):
        current_test_name = os.environ.get("PYTEST_CURRENT_TEST").split(":")[-1].split(" ")[0].replace("test_", "")
        filename = os.path.join(output_dir,
                                '{}_{}_page{}.jpeg'.format(current_test_name, self.page_name, unique_time_stamp()))
        self.w.save_screenshot(filename)

        return filename

    def refresh(self):
        return self.w.refresh()

