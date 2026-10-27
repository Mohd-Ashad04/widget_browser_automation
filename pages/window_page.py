from playwright.sync_api import Page, expect


class WindowPage:
    def __init__(self, page: Page):
        self.page = page

    def change_second_window_options(self):
        panel = self.page.get_by_role("tabpanel", name="Window")
        panel.get_by_role("tab", name="Page 2", exact=True).click()
        self.page.wait_for_timeout(400)
        second_window = self.page.get_by_role("dialog").filter(
            has=self.page.get_by_text("The second window", exact=True)
        )

        for name in ("Show Close", "Use resize frame", "Movable"):
            checkbox = second_window.get_by_role(
                "checkbox", name=name, exact=True
            )
            checkbox.click()
            self.page.wait_for_timeout(400)
            expect(checkbox).to_have_attribute("aria-checked", "false")
