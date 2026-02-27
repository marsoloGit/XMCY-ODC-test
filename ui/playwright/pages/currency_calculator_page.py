from ui.playwright.pages.base_page import BasePage
from ui.playwright.elements.searchable_dropdown import SearchableDropdown
import re
import allure


class CurrencyCalculatorPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "/forex-calculators/currency"

    @property
    def input_quantity(self):
        # return self.page.locator("#quantity")
        return self.page.get_by_label("Amount")

    @property
    def searchable_input_from_currency(self):
        return SearchableDropdown(self.page, self.page.locator("#currency_input").nth(0))

    @property
    def searchable_input_to_currency(self):
        return SearchableDropdown(self.page, self.page.locator("#currency_input").nth(1))

    @property
    def btn_convert(self):
        return self.page.locator("#button_xm-www-currency-converter").filter(has_text="Convert")

    @allure.step("Navigate to Currency Calculator")
    def navigate(self):
         self.page.goto(self.url)

    @allure.step("Convert currency")
    def convert(self, amount="100", from_curr="EUR", to_curr="USD"):
        self.input_quantity.fill(amount)
        self.searchable_input_from_currency.select(from_curr)
        self.searchable_input_to_currency.select(to_curr)
        self.btn_convert.click(force=True)

    def is_results_visible(self):
        try:
            # Look for common result indicators on XM calculators
            result_indicators = [
                ".results-area", 
                "h2:has-text('Results')", 
                "div:has-text('Result')", 
                "tr:has-text('Total')"
            ]
            for selector in result_indicators:
                if self.page.locator(selector).first.is_visible():
                    return True
            # Check if any text appeared that looks like a converted value
            return self.page.get_by_text(re.compile(r"\d+\.\d+")).count() > 0
        except Exception:
            return False
