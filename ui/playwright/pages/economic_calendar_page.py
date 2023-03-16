from ui.playwright.elements.date_picker import DatePicker
from ui.playwright.elements.slider import Slider


class EconomicCalendar:

    def __init__(self, page):
        self.page = page

    @property
    def slider(self):
        return Slider(
            self.page,
            css_slider='mat-slider[role=slider]',
            css_thumb='div.mat-slider-thumb',
            css_iframe='#iFrameResizer0',
        )

    @property
    def date_picker(self):
        return DatePicker(self.page)

    def navigate(self):
        self.page.goto('/research/economicCalendar')

    def move_slider_to(self, to_value):
        self.slider.move(to_value)
