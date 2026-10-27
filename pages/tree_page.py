from playwright.sync_api import Page, expect


class TreePage:
    selected_color = "rgb(61, 114, 201)"

    def __init__(self, page: Page):
        self.page = page

    def select_tree_and_virtual_tree_items(self):
        panel = self.page.get_by_role("tabpanel", name="Tree")

        tree = panel.get_by_text("Tree", exact=True).locator("+ div")
        for name in ("Files", "Workspace"):
            item = tree.get_by_text(name, exact=True)
            item.click()
            self.page.wait_for_timeout(400)
            expect(item.locator("..")).to_have_css(
                "background-color", self.selected_color
            )

        virtual_tree = panel.get_by_text("VirtualTree", exact=True).locator(
            "+ div"
        )
        for name in ("Network", "Trash"):
            item = virtual_tree.get_by_text(name, exact=True)
            item.click()
            self.page.wait_for_timeout(400)
            expect(item.locator("..")).to_have_css(
                "background-color", self.selected_color
            )
