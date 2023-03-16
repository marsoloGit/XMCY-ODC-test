from ui.selenium.pages.home_page import HomePage


class CookieModal:
    def __init__(self, page):
        self.page = page

    @property
    def modal_container(self):
        return self.page.locator("#cookieModal div.modal-content")

    @property
    def btn_accept_all(self):
        return self.modal_container.get_by_text("ACCEPT ALL")

    def accept_all_cookies(self):
        self.btn_accept_all.click()
        return HomePage(self.page)


