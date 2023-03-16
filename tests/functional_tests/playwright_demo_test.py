from testfixtures import compare
import pytest
from config.constants import CalendarRanges
from ui.playwright.pages.economic_calendar_page import EconomicCalendar


def test_check_flow_to_calendar(home_page_pw):
    research_and_education_page = home_page_pw.navigate_to_research_and_education()
    research_and_education_page.navigate_to_calendar()


date_range_names = [
    CalendarRanges.NEXT_WEEK,
    CalendarRanges.TOMORROW,
    CalendarRanges.TODAY,
    CalendarRanges.NEXT_MONTH,
]


@pytest.mark.parametrize("date_range_name", date_range_names)
def test_check_calendar_slider(date_range_name, home_page_pw, page):
    calendar_page = EconomicCalendar(page)
    calendar_page.navigate()
    calendar_page.move_slider_to(date_range_name.value)
    actual_dates_range = calendar_page.date_picker.get_selected_range()
    expected_dates_range = CalendarRanges.get_range(date_range_name)

    compare(actual=actual_dates_range, expected=expected_dates_range)
