from playwright.sync_api import Page, expect


class ListPage:
    selected_color = "rgb(61, 114, 201)"

    def __init__(self, page: Page):
        self.page = page

    def select_list_items(self):
        panel = self.page.get_by_role("tabpanel", name="List")
        lists = [
            panel.get_by_text("List", exact=True).locator("+ div"),
            panel.get_by_text("List (virtual)", exact=True).locator("+ div"),
            panel.get_by_text("List (virtual, grouped)", exact=True).locator(
                "+ div"
            ),
        ]

        for widget, name in zip(
            lists,
            ("Weidner, Ludwig", "Weidner, Ludwig", "Binder, Marita"),
        ):
            item = widget.get_by_text(name, exact=True)
            item.click()
            self.page.wait_for_timeout(400)
            expect(item.locator("..")).to_have_css(
                "background-color", self.selected_color
            )
