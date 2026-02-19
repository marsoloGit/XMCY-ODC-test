from ui.playwright.pages.base_page import BasePage
from ui.playwright.pages.economic_calendar_page import EconomicCalendar
from playwright.sync_api import expect


class ResearchEducationPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    @property
    def lnk_economic_calendar(self):
        return self.page.get_by_role(role='link', name="Economic Calendar")

    def navigate_to_calendar(self):
        self.lnk_economic_calendar.click()
        return EconomicCalendar(self.page)
