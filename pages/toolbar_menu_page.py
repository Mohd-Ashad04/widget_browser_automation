from playwright.sync_api import Page, expect


class ToolbarMenuPage:
    def __init__(self, page: Page):
        self.page = page

    def use_toolbar_and_sidebar_menus(self):
        panel = self.page.get_by_role("tabpanel", name="Toolbar/Menu")
        menu_button = panel.get_by_role(
            "button", name="Toolbar MenuButton", exact=True
        )
        menu_button.locator('div[style*="arrows/down.gif"]').click()
        self.page.wait_for_timeout(400)

        menu_id = menu_button.get_attribute("aria-controls")
        menu = self.page.locator(f'div[role="menu"].qx-main#{menu_id}')
        menu.get_by_role("menuitem", name="Menu MenuButton", exact=True).click()
        self.page.wait_for_timeout(400)

        heading = panel.get_by_text("Menu (with slidebar)", exact=True)
        sidebar = heading.locator("..").get_by_role("menu")
        viewport = sidebar.locator(
            '[aria-orientation="vertical"] > div'
        ).first
        radio = sidebar.get_by_role(
            "menuitem", name="Menu RadioButton", exact=True
        ).first
        viewport.hover()
        self.page.mouse.wheel(0, 300)
        self.page.wait_for_timeout(3000)

        radio.click(force=True)
        expect(radio).to_have_attribute("aria-checked", "true")
        self.page.wait_for_timeout(400)
        self.page.get_by_role("tab", name="Window", exact=True).click()
        self.page.wait_for_timeout(400)
