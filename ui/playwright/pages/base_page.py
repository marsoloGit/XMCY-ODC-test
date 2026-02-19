from ui.playwright.elements.menu_block import DesktopMenuBlock


class BasePage:
    def __init__(self, page):
        self.page = page

    @property
    def desktop_menu(self):
        return DesktopMenuBlock(self.page)
