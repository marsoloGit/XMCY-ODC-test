from ui.selenium.elements.common_elements import Element, Elements
from ui.selenium.components.container import Container
from ui.selenium.pages.home_page import HomePage


class ModalDialog(Container):
    modal_container = Element(css="xm-cookie-modal-main")
    modal_text = Element(css="section.modal-body", context=True)
    modal_buttons = Elements(css="button", context=True)

    def get_modal_text(self):
        text = self.modal_text(self.modal_container).text
        return text

    def click_dialog_button_by_text(self, text):
        return self.click_container_element_by_text(
            self.modal_buttons(self.modal_container),
            text,
        )


class CookieModal(ModalDialog):
    def accept_all_cookies(self):
        self.click_dialog_button_by_text('Accept All')
        return HomePage(self.w)
