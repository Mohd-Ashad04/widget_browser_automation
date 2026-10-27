from playwright.sync_api import Page, expect


class FormPage:
    def __init__(self, page: Page):
        self.page = page

    def fill_name(self):
        text_field = self.page.get_by_placeholder("required")
        text_field.fill("Mohd Ashad")
        expect(text_field).to_have_value("Mohd Ashad")
        self.page.wait_for_timeout(400)

    def fill_password(self):
        password_field = self.page.get_by_placeholder("password")
        password_field.fill("Test@12345")
        expect(password_field).to_have_value("Test@12345")
        self.page.wait_for_timeout(400)

    def select_combo_box_item_9(self):
        combo_box = self.page.get_by_role("combobox")
        combobox = combo_box.get_by_placeholder("Pick an item")
        combo_box.get_by_role("button").click()

        popup = self.page.locator(".qx-popup:visible").last
        popup.hover()
        option = popup.get_by_role("option", name="Item 9", exact=True)
        self.page.mouse.wheel(0, 3000)

        expect(option).to_be_visible()
        option.click()
        expect(combobox).to_have_value("Item 9")
        self.page.wait_for_timeout(400)

    def select_virtual_combo_box_item_299(self):
        virtual_widget = self.page.get_by_text(
            "VirtualComboBox :", exact=True
        ).locator("+ div")
        virtual_combobox = virtual_widget.get_by_placeholder("Pick an item")
        virtual_widget.get_by_role("button").click()
        popup = self.page.locator(".qx-popup:visible").last
        popup.locator(":scope > div > div").first.hover()
        option = popup.get_by_text("Item 299", exact=True)
        for _ in range(250):
            self.page.mouse.wheel(0, 3000)
            self.page.wait_for_timeout(10)
            if option.is_visible():
                option.click(force=True)
                break
        else:
            raise AssertionError("Item 299 did not become visible in the dropdown.")

        expect(virtual_combobox).to_have_value("Item 299")
        self.page.wait_for_timeout(400)
