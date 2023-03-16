from enum import Enum
import datetime
import calendar


class CalendarRanges(Enum):
    TODAY = 1
    TOMORROW = 2
    THIS_WEEK = 3
    NEXT_WEEK = 4
    THIS_MONTH = 5
    NEXT_MONTH = 6

    @classmethod
    def get_range(cls, name):
        dates_range = []
        today = datetime.date.today()

        def get_all_dates_in_month(given_date):
            month = getattr(given_date, 'month')
            year = getattr(given_date, 'year')
            number_of_days = calendar.monthrange(year, month)[1]
            first_date = datetime.date(year, month, 1)
            last_date = datetime.date(year, month, number_of_days)
            delta = last_date - first_date
            return [(first_date + datetime.timedelta(days=i)) for i in range(delta.days + 1)]

        def get_all_dates_in_week_by_date(given_date):
            return [given_date + datetime.timedelta(days=i) for i in range(0 - today.weekday(), 7 - today.weekday())]

        if name == cls.TODAY:
            dates_range.append(today)
        elif name == cls.TOMORROW:
            tomorrow = today + datetime.timedelta(days=1)
            dates_range.append(tomorrow)
        elif name == cls.THIS_WEEK:
            dates_range = get_all_dates_in_week_by_date(today)
        elif name == cls.NEXT_WEEK:
            dt_one_week_from_today = today + datetime.timedelta(days=7)
            dates_range = get_all_dates_in_week_by_date(dt_one_week_from_today)
        elif name == cls.THIS_MONTH:
            dates_range = get_all_dates_in_month(today)
        elif name == cls.NEXT_MONTH:
            dt_fst_day_in_next_month = (today.replace(day=1) + datetime.timedelta(days=32)).replace(day=1)
            dates_range = get_all_dates_in_month(dt_fst_day_in_next_month)
        return [date.strftime("%a %b %d %Y") for date in dates_range]


class BrowserType(Enum):
    CHROME = 'chromium'
    FIREFOX = 'firefox'
    WEBKIT = 'webkit'
