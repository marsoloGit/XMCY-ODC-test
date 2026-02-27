import re
import allure

class SearchableDropdown:
    def __init__(self, page, locator):
        self.page = page
        self.locator = locator
        # Common results selectors for searchable dropdowns
        self.results_selector = "div.cursor-pointer, li, [role='option'], [role='menuitem']"

    @allure.step("Search and select '{value}'")
    def select(self, value):
        self.locator.click()
        self.locator.fill("")
        # Type with delay to trigger search
        self.locator.type(value, delay=100)
        
        # Wait for results to appear and click the first matching one
        result = self.page.locator(self.results_selector).filter(has_text=re.compile(rf"\s*{re.escape(value)}\s*")).first
        # Ensure it's visible before clicking
        result.wait_for(state="visible", timeout=10000)
        result.click(force=True)
