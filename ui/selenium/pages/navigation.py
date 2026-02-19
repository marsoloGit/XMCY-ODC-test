from ui.selenium.pages.base_bage import BasePage
from ui.selenium.pages.economic_calendar_page import EconomicCalendar
from config import settings as s


class Navigation(BasePage):

    def navigate_to_economic_calendar(self):
        self.get('/economic-calendar')
        self.w.set_page_load_timeout(s.WEBDRIVER_ELEMENT_WAIT)
        return EconomicCalendar(self.w)
