

class MenuBlock:
    def __init__(self, page):
        self.page = page
        self.links_block = self.page.locator("xm-sidebar-navigation")
        self.links = self.links_block.locator("a, button")

    def click_link_by_text(self, text):
        return self.click_container_element_by_text(self.links, text, )

    def click_container_element_by_text(self, elements, text):
        found = False
        try:
            for el in elements.all():
                # text_content() sees text even if hidden, inner_text() only if visible
                if el.text_content().strip().lower() == text.lower():
                    el.click()
                    found = True
                    break
            if not found:
                raise Exception(f"Element with text '{text}' not found in the menu block")
        except Exception as e:
            self.page.screenshot()
            raise e

class DesktopMenuBlock(MenuBlock):
    def __init__(self, page):
        super().__init__(page)
        self.links_block = self.page.locator("header nav")
        # Sub-menu items like 'Economic Calendar' are rendered in global overlays
        self.links = self.page.locator("header nav a, header nav button, .cdk-overlay-container a, .cdk-overlay-container button")
