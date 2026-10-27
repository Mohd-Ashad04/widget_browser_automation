from playwright.sync_api import Page


class TabPage:
    def __init__(self, page: Page):
        self.page = page

    def select_calculator_and_notes_tabs(self):
        panel = self.page.get_by_role("tabpanel", name="Tab")

        top = panel.locator(
            '[role="tablist"]:has([role="tab"].qx-tabview-page-button-top)'
        )
        top.get_by_role("tab", name="Calculator", exact=True).click()
        self.page.wait_for_timeout(400)

        left = panel.locator(
            '[role="tablist"]:has([role="tab"].qx-tabview-page-button-left)'
        )
        left.get_by_role("tab", name="Calculator", exact=True).click()
        self.page.wait_for_timeout(400)

        for side in ("bottom", "right"):
            section = panel.locator(
                f'[role="tablist"]:has([role="tab"].qx-tabview-page-button-{side})'
            )
            section.get_by_role("tab", name="Notes", exact=True).click()
            self.page.wait_for_timeout(400)
