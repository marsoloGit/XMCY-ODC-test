import allure
from testfixtures import compare
import pytest
from config.constants import CalendarRanges
from ui.playwright.pages.economic_calendar_page import EconomicCalendar


@allure.id("4")
@allure.title('Check flow to calendar playwright')
def test_check_flow_to_calendar(home_page_pw, page):
    # Menu accessible from home_page
    home_page_pw.desktop_menu.click_link_by_text('Discover')
    home_page_pw.desktop_menu.click_link_by_text('Economic Calendar')
    # Verify we are on the calendar page
    calendar_page = EconomicCalendar(page)
    # Even if we are already on the calendar page, the menu is still there!
    calendar_page.desktop_menu.click_link_by_text('Trading')



date_range_names = [
    CalendarRanges.NEXT_WEEK,
    CalendarRanges.TOMORROW,
    CalendarRanges.TODAY,
    CalendarRanges.NEXT_MONTH,
]


@allure.id("1")
@allure.title('Check calendar slider playwright')
@pytest.mark.parametrize("date_range_name", date_range_names)
def test_check_calendar_slider(date_range_name, home_page_pw, page):
    calendar_page = EconomicCalendar(page)
    calendar_page.navigate()
    calendar_page.move_slider_to(date_range_name.value)
    actual_dates_range = calendar_page.date_picker.get_selected_range()
    expected_dates_range = CalendarRanges.get_range(date_range_name)

    compare(actual=actual_dates_range, expected=expected_dates_range)