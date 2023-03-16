from ui.selenium.pages.base_bage import BasePage


class Container(BasePage):

    def click_container_element_by_text(self, elements, text):
        try:
            for el in elements:
                if el.text.strip() == text:
                    el.click()
                    break
        except Exception as e:
            self.save_screenshot()
            raise e
