import allure

from ui.selenium.components.menu_block import UpperMenuBlock
import pytest
from config.constants import CalendarRanges
from testfixtures import compare


@allure.id("3")
@allure.title('Check flow to calendar selenium')
def test_check_flow_to_calendar(home_page):
    UpperMenuBlock(home_page.w).click_link_by_text('Economic Calendar')


date_range_names = [
    CalendarRanges.NEXT_WEEK,
    CalendarRanges.TOMORROW,
    CalendarRanges.TODAY,
    CalendarRanges.NEXT_MONTH,
]


@allure.id("2")
@pytest.mark.parametrize("date_range_name", date_range_names)
@allure.title('Check calendar slider selenium')
def test_check_calendar_slider(home_page, site_navigation, date_range_name):
    CalendarRanges.get_range(CalendarRanges.TOMORROW)
    calendar_page = site_navigation.navigate_to_economic_calendar()
    calendar_page.move_slider_to(date_range_name.value)
    actual_dates_range = calendar_page.date_picker.get_selected_range()
    expected_dates_range = CalendarRanges.get_range(date_range_name)

    compare(actual=actual_dates_range, expected=expected_dates_range)