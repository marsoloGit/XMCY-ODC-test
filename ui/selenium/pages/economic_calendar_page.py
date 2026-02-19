from ui.selenium.elements.common_elements import Slider
from ui.selenium.components.date_picker import DatePicker
from ui.selenium.pages.base_bage import BasePage


class EconomicCalendar(BasePage):
    page_name = "Economic Calendar"

    def __init__(self, webdriver):
        super(EconomicCalendar, self).__init__(webdriver)
        self.date_picker = DatePicker(webdriver)

    slider = Slider(
        css='mat-slider',
        iframe_css='iframe[title="Economic Calendar"]',
        thumb_container_css='.mdc-slider__thumb',
        input_range_css='input[type="range"]',
    )

    def move_slider_to(self, to_value):
        self.slider = to_value
        self.w.switch_to.default_content()
