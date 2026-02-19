from ui.selenium.elements.common_elements import Element
from ui.selenium.pages.base_bage import BasePage
from ui.selenium.pages.research_and_education_page import ResearchEducationPage
from config import settings as s


class HomePage(BasePage):
    page_name = "Home Page"
    lnk_research_and_education = Element(css="button[id*='button_xm-www-layout']")

    def navigate_to_research_and_education(self):
        self.w.set_script_timeout(s.WEBDRIVER_ELEMENT_WAIT)
        self.lnk_research_and_education.click()
        return ResearchEducationPage(self.w)
