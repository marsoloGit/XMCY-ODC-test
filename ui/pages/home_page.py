from ui.Elements.common_elements import Element
from ui.pages.base_bage import BasePage
from ui.pages.research_and_education_page import ResearchEducationPage


class HomePage(BasePage):

    page_name = "Home Page"
    lnk_research_and_education = Element(link_text="RESEARCH & EDUCATION")


    def navigate_to_research_and_education(self):
        self.lnk_research_and_education.click()
        return ResearchEducationPage(self.w)



