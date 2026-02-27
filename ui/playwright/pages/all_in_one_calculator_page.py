from ui.playwright.pages.base_page import BasePage
from ui.playwright.elements.dropdown import Dropdown
from ui.playwright.elements.searchable_dropdown import SearchableDropdown
import re
import allure


class AllInOneCalculatorPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "/forex-calculators/all-in-one"

    @property
    def dropdown_account_base_currency(self):
        return Dropdown(self.page, self.page.locator("#button_xm-www-account-base-currency-field"))

    @property
    def dropdown_leverage(self):
        return Dropdown(self.page, self.page.locator("#button_xm-www-leverage-for-margin-field"))

    @property
    def dropdown_account_type(self):
        return Dropdown(self.page, self.page.locator("#button_xm-www-account-type-field"))

    @property
    def searchable_input_symbol(self):
        return SearchableDropdown(self.page, self.page.locator("#currencyPair_input"))

    @property
    def input_volume(self):
        return self.page.locator("#volumeInLots")

    @property
    def btn_calculate(self):
        return self.page.locator("#button_xm-www-all-in-one-calculator").filter(has_text="Calculate")

    @allure.step("Navigate to All-in-One Calculator")
    def navigate(self):
        self.page.goto(self.url, wait_until="load")
        self.page.wait_for_selector("#button_xm-www-leverage-for-margin-field", state="visible", timeout=30000)

    @allure.step("Fill All-in-One form")
    def fill_form(self, currency="EUR", leverage="1:1", account_type="Standard", symbol="EURUSD", volume="1"):
        self.dropdown_account_base_currency.select(currency)
        self.dropdown_leverage.select(leverage)
        self.dropdown_account_type.select(account_type)
        self.searchable_input_symbol.select(symbol)
        self.input_volume.fill(volume)

    @allure.step("Click Calculate")
    def calculate(self):
        self.btn_calculate.click(force=True)

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
            # Check if any text appeared that looks like a numeric value
            return self.page.get_by_text(re.compile(r"\d+\.\d+")).count() > 0
        except Exception:
            return False
