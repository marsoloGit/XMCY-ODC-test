from ui.playwright.pages.base_page import BasePage
from ui.playwright.pages.research_and_education_page import ResearchEducationPage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @property
    def lnk_research_and_education(self):
        return self.page.get_by_role(role='link', name="RESEARCH & EDUCATION")

    def navigate_to_research_and_education(self):
        self.lnk_research_and_education.click()
        return ResearchEducationPage(self.page)
