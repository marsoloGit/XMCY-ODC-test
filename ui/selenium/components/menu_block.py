from ui.selenium.elements.common_elements import Element, Elements
from ui.selenium.components.container import Container


class MenuBlock(Container):
    links_block = Element(css="xm-sidebar-navigation")
    links = Elements(css="a, button", context=True)

    def click_link_by_text(self, text):
        return self.click_container_element_by_text(self.links(self.links_block), text, )


class ResearchMenuBlock(MenuBlock):
    links_block = Element(xpath="//div[contains(@class, 'block') and .//span/i[contains(@class, 'xmChart-search')]]")


class UpperMenuBlock(MenuBlock):
    links_block = Element(css="header nav")
    links = Elements(css="a, button", context=True)