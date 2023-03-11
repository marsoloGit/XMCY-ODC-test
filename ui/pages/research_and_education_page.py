from ui.components.menu_block import ResearchMenuBlock
from ui.pages.base_bage import BasePage
from ui.pages.economic_calendar_page import EconomicCalendar


class ResearchEducationPage(BasePage):
    page_name = "Research&Education page"

    def __init__(self, webdriver):
        super(ResearchEducationPage, self).__init__(webdriver)
        self.search_menu_block = ResearchMenuBlock(webdriver)

    def navigate_to_calendar(self):
        self.search_menu_block.click_link_by_text('Economic Calendar')
        return EconomicCalendar(self.w)

