from ui.playwright.pages.research_and_education_page import ResearchEducationPage


class HomePage:
    def __init__(self, page):
        self.page = page

    @property
    def lnk_research_and_education(self):
        return self.page.get_by_role(role='link', name="RESEARCH & EDUCATION")

    def navigate_to_research_and_education(self):
        self.lnk_research_and_education.click()
        return ResearchEducationPage(self.page)
