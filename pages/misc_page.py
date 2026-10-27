from playwright.sync_api import Page, expect


class MiscPage:
    selected_color = "rgb(61, 114, 201)"

    def __init__(self, page: Page):
        self.page = page

    def select_items(self):
        panel = self.page.get_by_role("tabpanel", name="Misc")
        for name in ("Item 5", "Item 8"):
            item = panel.get_by_text(name, exact=True)
            item.click()
            self.page.wait_for_timeout(400)
            expect(item.locator("..")).to_have_css(
                "background-color", self.selected_color
            )
        print("Misc: selected Item 5 and Item 8.")
