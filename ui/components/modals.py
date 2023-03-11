from ui.elements.common_elements import Element, Elements
from ui.components.container import Container
from ui.pages.home_page import HomePage


class ModalDialog(Container):
    modal_container = Element(css="div.modal-content")
    modal_text = Element(css="div.modal-body", context=True)
    modal_buttons = Elements(css="button.btn", context=True)

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
        self.click_dialog_button_by_text('ACCEPT ALL')
        return HomePage(self.w)
