from ui.Elements.common_elements import Element, Elements
from ui.components.container import Container


class DatePicker(Container):

    date_buttons = Elements(context=True, css='button.mat-calendar-body-cell')
    date_picker_container = Element(css='mat-calendar.mat-calendar', iframe_id_='iFrameResizer0')

    def __init__(self, webdriver):
        super(DatePicker, self).__init__(webdriver=webdriver)

    def get_selected_range(self):

        dates_range = []
        for button in self.date_buttons(self.date_picker_container):
            if 'in-range' in button.get_attribute('class') or 'active' in button.get_attribute('class'):
                dates_range.append(button.get_attribute('aria-label'))

        return dates_range
