from playwright.sync_api import Page, expect


class BasicPage:
    def __init__(self, page: Page):
        self.page = page

    def toggle_disabled_and_check_atom(self):
        panel = self.page.get_by_role("tabpanel", name="Basic")
        button = panel.get_by_role("button", name="Disabled")
        button.click()
        self.page.wait_for_timeout(400)
        expect(button).to_have_attribute("aria-pressed", "true")
        expect(panel.get_by_text("Atom", exact=True)).to_be_visible()
        print("Basic: toggled Disabled and checked the Atom example.")
