from playwright.sync_api import Page, expect


class TablePage:
    selected_color = "rgb(61, 114, 201)"

    def __init__(self, page: Page):
        self.page = page

    def select_rows_and_sort_columns(self):
        table = self.page.get_by_role("tabpanel", name="Table").get_by_role(
            "grid"
        )
        rows = table.get_by_role("row")
        row_0, row_1, row_2 = rows.nth(1), rows.nth(2), rows.nth(3)

        row_0.click()
        self.page.wait_for_timeout(400)
        row_1.click()
        self.page.wait_for_timeout(400)
        expect(row_1).to_have_css("background-color", self.selected_color)
        expect(row_0).not_to_have_css(
            "background-color", self.selected_color
        )
        expect(row_2).not_to_have_css(
            "background-color", self.selected_color
        )

        table.get_by_role("columnheader", name="ID", exact=True).click()
        self.page.wait_for_timeout(400)
        table.get_by_role(
            "columnheader", name="A number", exact=True
        ).click()
        self.page.wait_for_timeout(400)
