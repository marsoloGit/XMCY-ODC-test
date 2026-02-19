
class Slider:
    def __init__(self, page, css_slider, css_slider_input, css_iframe=None):
        self.page = page
        if css_iframe:
            element_container = page.frame_locator(css_iframe)
        else:
            element_container = page
        self.slider = element_container.locator(css_slider)
        self.slider_input = element_container.locator(css_slider_input)
        self.min = int(self.slider_input.get_attribute("min"))
        self.max = int(self.slider_input.get_attribute("max"))

        # Wait for slider to be visible to ensure bounding box is available
        self.slider.wait_for(state='visible')
        self.box = self.slider.bounding_box()
        self.slide_step = self.box['width'] / (self.max - self.min)

    def move(self, value):
        x_offset = round(self.slide_step * value)
        # click the position (Playwright counts from the top-left corner!)
        self.slider.click(position={
            "x": x_offset,
            "y": self.box['height'] / 2
        })