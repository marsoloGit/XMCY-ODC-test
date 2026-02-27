import re
import allure

class Dropdown:
    def __init__(self, page, locator):
        self.page = page
        self.locator = locator
        # Common options for XM calculators
        self.option_selector = ".cdk-menu-item, [role='menuitem'], [role='option'], .cursor-pointer"

    @allure.step("Select '{value}' from dropdown")
    def select(self, value):
        self.locator.click()
        # Minor wait for the animation/overlay to stabilize
        self.page.wait_for_timeout(1000)
        
        # Try finding the item in the overlay first
        try:
             # Match exact or with whitespace
             item = self.page.locator(self.option_selector).filter(has_text=re.compile(rf"^\s*{re.escape(value)}\s*$")).first
             item.click(force=True, timeout=5000)
        except Exception:
             # Fallback: looser search in case of leverage (e.g. "500" matching "1:500")
             lev_val = value.split(":")[-1] if ":" in value else value
             self.page.get_by_text(re.compile(rf"{re.escape(lev_val)}")).last.click(force=True)
