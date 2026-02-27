import allure
import pytest

from ui.playwright.pages.currency_calculator_page import CurrencyCalculatorPage


@allure.title("Check All-in-One Calculator")
def test_all_in_one_calculator(home_page_pw, all_in_one_calc_page):
    all_in_one_calc_page.navigate()
    all_in_one_calc_page.fill_form(
        currency="EUR",
        leverage="1:30",
        account_type="Standard",
        symbol="EURUSD",
        volume="1"
    )
    all_in_one_calc_page.calculate()
    assert all_in_one_calc_page.is_results_visible(), "Results area should be visible after calculation"


@allure.title("Check Currency Calculator")
def test_currency_calculator(home_page_pw, page):
    currency_calc_page = CurrencyCalculatorPage(page)
    currency_calc_page.navigate()
    currency_calc_page.convert(
        amount="500",
        from_curr="USD",
        to_curr="EUR"
    )
    assert currency_calc_page.is_results_visible(), "Results area should be visible after conversion"
