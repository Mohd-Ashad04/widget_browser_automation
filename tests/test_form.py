from playwright.sync_api import sync_playwright

from pages.form_page import FormPage


def test_form_demo():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(
            "https://qooxdoo.org/qxl.widgetbrowser/",
            wait_until="domcontentloaded",
        )

        form_page = FormPage(page)
        form_page.fill_name()
        form_page.fill_password()
        form_page.select_combo_box_item_9()
        form_page.select_virtual_combo_box_item_299()

        browser.close()
