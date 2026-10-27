from playwright.sync_api import Page


class EmbedPage:
    def __init__(self, page: Page):
        self.page = page

    def scroll_embedded_content(self):
        html = self.page.get_by_role("tabpanel", name="Embed").locator(
            ".qx-main"
        ).filter(has_text="Lorem ipsum dolor sit amet").last
        html.hover()
        self.page.mouse.wheel(0, 3000)
        self.page.wait_for_timeout(400)
        self.page.mouse.wheel(0, 3000)
        self.page.wait_for_timeout(400)
        print("Embed: scrolled the HTML text.")
