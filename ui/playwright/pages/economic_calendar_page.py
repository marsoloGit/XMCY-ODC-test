from ui.playwright.pages.base_page import BasePage
from ui.playwright.elements.date_picker import DatePicker
from ui.playwright.elements.slider import Slider


class EconomicCalendar(BasePage):

    def __init__(self, page):
        super().__init__(page)

    @property
    def slider(self):
        return Slider(
            self.page,
            css_slider='.mdc-slider',
            css_slider_input='input[type="range"]',
            css_iframe='iframe[title="Economic Calendar"]',
        )

    @property
    def date_picker(self):
        return DatePicker(self.page)

    def navigate(self):
        self.page.goto('/research/economicCalendar',
                       wait_until="domcontentloaded",
                       timeout=60000,
                       )

    def move_slider_to(self, to_value):
        self.slider.move(to_value)
