

class DatePicker:
    def __init__(self, page):
        self.page = page
        self.date_buttons = self.page.frame_locator('iframe[title="Economic Calendar"]').locator('button.mat-calendar-body-cell')

    def get_selected_range(self):

        dates_range = []
        for button in self.date_buttons.all():
            if 'in-range' in button.get_attribute('class') or 'active' in button.get_attribute('class'):
                dates_range.append(button.get_attribute('aria-label'))

        return dates_range
