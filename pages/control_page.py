from playwright.sync_api import Page, expect


class ControlPage:
    def __init__(self, page: Page):
        self.page = page

    def select_red_color(self):
        panel = self.page.get_by_role("tabpanel", name="Control")
        panel.locator('[style*="background-color:red"]').click()
        self.page.wait_for_timeout(400)
        expect(panel.get_by_role("textbox").first).to_have_value("FF0000")
        print("Control: selected the red color preset.")
