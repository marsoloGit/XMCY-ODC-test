
from ui.elements.common_elements import Slider
from ui.components.date_picker import DatePicker
from ui.pages.base_bage import BasePage


class EconomicCalendar(BasePage):

    page_name = "Economic Calendar"

    def __init__(self, webdriver):
        super(EconomicCalendar, self).__init__(webdriver)
        self.date_picker = DatePicker(webdriver)

    slider = Slider(
        css ='mat-slider[role=slider]',
        iframe_id_ = 'iFrameResizer0',
        thumb_container_css='mat-slider[role=slider] div.mat-slider-thumb',
    )

    def move_slider_to(self, to_value):
        self.slider = to_value
        self.w.switch_to.default_content()










