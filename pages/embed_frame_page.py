from playwright.sync_api import Page, expect


class EmbedFramePage:
    def __init__(self, page: Page):
        self.page = page

    def scroll_embedded_frames(self):
        frames = self.page.get_by_role(
            "tabpanel", name="EmbedFrame"
        ).locator("iframe")
        for index in range(2):
            frame = frames.nth(index)
            frame.hover(force=True)
            self.page.mouse.wheel(0, 300)
            self.page.wait_for_timeout(400)
        expect(frames).to_have_count(2)
        print("EmbedFrame: scrolled over both embedded frames.")
