import time
from page_objects import PageElement, MultiPageElement, _LOCATOR_MAP
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from config import settings as s

ELEMENT_TIMEOUT = s.WEBDRIVER_ELEMENT_WAIT


class Element(PageElement):
    def __init__(self, context=False, wait_time=ELEMENT_TIMEOUT, **kwargs):
        if not kwargs:
            raise ValueError("Please specify a locator")

        self.has_context = bool(context)
        self.wait_time = wait_time
        self.iframe_locator = None
        self.el_locator = None

        for k, v in kwargs.items():
            if 'iframe' in k:
                k = k.removeprefix('iframe_')
                self.iframe_locator = (_LOCATOR_MAP[k], v)
            else:
                if k in _LOCATOR_MAP:
                    self.el_locator = (_LOCATOR_MAP[k], v)

    def find(self, context):
        try:
            if self.iframe_locator:
                WebDriverWait(context, self.wait_time).until(
                    EC.frame_to_be_available_and_switch_to_it((self.iframe_locator)))

            return WebDriverWait(context, self.wait_time).until(EC.presence_of_element_located(self.el_locator))

        except TimeoutException:
            return None
        except NoSuchElementException:
            pass


class Slider(Element):
    def __init__(self, context=False, wait_time=ELEMENT_TIMEOUT, **kwargs):
        super(Slider, self).__init__(context, **kwargs)
        self.wait_time = wait_time
        self.thumb_container_locator = None
        self.min = 0
        self.max = 0

        for k, v in kwargs.items():
            if 'thumb_container' in k:
                k = k.removeprefix('thumb_container_')
                self.thumb_container_locator = (_LOCATOR_MAP[k], v)

    def __set__(self, instance, value):
        if self.has_context:
            raise ValueError("Sorry, the set descriptor doesn't support elements with context.")

        slider = self.__get__(instance, instance.__class__)
        time.sleep(2)
        self.min = int(slider.get_attribute('aria-valuemin'))
        self.max = int(slider.get_attribute('aria-valuemax'))
        slide_step = slider.size['width'] / (self.max - self.min)

        x_offset = round(slide_step * value)
        # set el_locator to be thumb one so that to give it focus
        temp = self.el_locator
        self.el_locator = self.thumb_container_locator

        instance.w.switch_to.default_content()
        slider_thumb = self.__get__(instance, instance.__class__)

        if not slider_thumb:
            raise ValueError("Can't set value, slider thumb not found")

        action = ActionChains(instance.w)
        action.click_and_hold(slider_thumb)
        instance.w.set_script_timeout(ELEMENT_TIMEOUT)
        action.move_by_offset(x_offset, 0).release().perform()

        # set el_locator back to slider
        self.el_locator = temp


class Input(Element):
    def clear(self, instance):
        if self.has_context:
            raise ValueError("Sorry, the set descriptor doesn't support elements with context.")
        elem = self.__get__(instance, instance.__class__)
        if not elem:
            raise ValueError("Can't set value, element not found")
        elem.clear()


class Elements(MultiPageElement):
    def __init__(self, context=False, wait_time=ELEMENT_TIMEOUT, **kwargs):
        super(Elements, self).__init__(context, **kwargs)
        self.wait_time = wait_time

    def find(self, context):
        try:
            return WebDriverWait(context, self.wait_time).until(EC.presence_of_all_elements_located(self.locator))
        except (NoSuchElementException, TimeoutException):
            return []
