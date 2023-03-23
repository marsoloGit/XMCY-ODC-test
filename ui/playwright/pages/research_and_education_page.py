from ui.playwright.pages.economic_calendar_page import EconomicCalendar
from playwright.sync_api import expect


class ResearchEducationPage:

    def __init__(self, page):
        self.page = page

    @property
    def lnk_economic_calendar(self):
        return self.page.get_by_role(role='link', name="Economic Calendar")

    def navigate_to_calendar(self):
        self.lnk_economic_calendar.click()
        return EconomicCalendar(self.page)
