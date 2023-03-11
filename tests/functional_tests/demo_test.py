import time

import pytest
from config.constants import CalendarRanges
from testfixtures import compare


def test_check_flow_to_calendar(home_page):
    research_and_education_page = home_page.navigate_to_research_and_education()
    research_and_education_page.navigate_to_calendar()
    assert 1 == 0


date_range_names = [
    CalendarRanges.NEXT_WEEK,
    CalendarRanges.TOMORROW,
    CalendarRanges.TODAY,
    CalendarRanges.NEXT_MONTH,
]


@pytest.mark.parametrize("date_range_name", date_range_names)
def test_check_calendar_slider(home_page, site_navigation, date_range_name):
    calendar_page = site_navigation.navigate_to_economic_calendar()
    calendar_page.move_slider_to(date_range_name.value)
    time.sleep(2)
    actual_dates_range = calendar_page.date_picker.get_selected_range()
    expected_dates_range = CalendarRanges.get_range(date_range_name)

    compare(actual=actual_dates_range, expected=expected_dates_range)
