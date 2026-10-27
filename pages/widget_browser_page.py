from playwright.sync_api import Page


class WidgetBrowserPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(
            "https://qooxdoo.org/qxl.widgetbrowser/",
            wait_until="domcontentloaded",
        )

    def navigate_to_demo(self, name: str):
        self.page.get_by_role("tab", name=name, exact=True).click()
        self.page.wait_for_timeout(400)
