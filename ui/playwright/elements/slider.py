import time


class Slider:
    def __init__(self, page, css_slider, css_thumb, css_iframe=None):
        self.page = page
        if css_iframe:
            element_container =  page.frame_locator(css_iframe)
        else:
            element_container = page
        self.slider = element_container.locator(css_slider)
        self.thumb = self.slider.locator(css_thumb)
        self.min = int(self.slider.get_attribute('aria-valuemin'))
        self.max = int(self.slider.get_attribute('aria-valuemax'))
        self.slide_step = self.slider.bounding_box()['width'] / (self.max - self.min)

    def move(self, value):
        x_offset = round(self.slide_step * value)
        box = self.slider.bounding_box()
        self.page.mouse.move(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
        self.page.mouse.down()
        time.sleep(2)
        self.page.mouse.move(box["x"] + x_offset, box["y"])
        self.page.mouse.up()


