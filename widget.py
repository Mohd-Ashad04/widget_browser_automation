from playwright.sync_api import expect, sync_playwright


url = "https://qooxdoo.org/qxl.widgetbrowser/"
selected_color = "rgb(61, 114, 201)"


def form_page(page):
    # Form
    text_field = page.get_by_placeholder("required")
    text_field.fill("Mohd Ashad")
    expect(text_field).to_have_value("Mohd Ashad")
    page.wait_for_timeout(400)

    password_field = page.get_by_placeholder("password")
    password_field.fill("Test@12345")
    expect(password_field).to_have_value("Test@12345")
    page.wait_for_timeout(400)

    combo_box = page.get_by_role("combobox")
    combobox = combo_box.get_by_placeholder("Pick an item")
    combo_box.get_by_role("button").click()

    popup = page.locator(".qx-popup:visible").last
    popup.hover()
    option = popup.get_by_role("option", name="Item 9", exact=True)
    page.mouse.wheel(0, 3000)

    option.click()
    expect(combobox).to_have_value("Item 9")
    page.wait_for_timeout(400)

    virtual_widget = page.get_by_text(
        "VirtualComboBox :", exact=True
    ).locator("+ div")
    virtual_combobox = virtual_widget.get_by_placeholder("Pick an item")
    virtual_widget.get_by_role("button").click()
    popup = page.locator(".qx-popup:visible").last
    popup.locator(":scope > div > div").first.hover()
    option = popup.get_by_text("Item 299", exact=True)
    for _ in range(250):
        page.mouse.wheel(0, 3000)
        page.wait_for_timeout(10)
        if option.count():
            option.click(force=True)
            break

    expect(virtual_combobox).to_have_value("Item 299")
    page.wait_for_timeout(400)


def tree_page(page):
    # Tree and Virtual Tree
    page.get_by_role("tab", name="Tree", exact=True).click()
    page.wait_for_timeout(400)
    panel = page.get_by_role("tabpanel", name="Tree")

    tree = panel.get_by_text("Tree", exact=True).locator("+ div")
    for name in ("Files", "Workspace"):
        item = tree.get_by_text(name, exact=True)
        item.click()
        page.wait_for_timeout(400)
        expect(item.locator("..")).to_have_css(
            "background-color", selected_color
        )

    virtual_tree = panel.get_by_text("VirtualTree", exact=True).locator(
        "+ div"
    )
    for name in ("Network", "Trash"):
        item = virtual_tree.get_by_text(name, exact=True)
        item.click()
        page.wait_for_timeout(400)
        expect(item.locator("..")).to_have_css(
            "background-color", selected_color
        )


def list_page(page):
    # List
    page.get_by_role("tab", name="List", exact=True).click()
    page.wait_for_timeout(400)
    panel = page.get_by_role("tabpanel", name="List")
    lists = [
        panel.get_by_text("List", exact=True).locator("+ div"),
        panel.get_by_text("List (virtual)", exact=True).locator("+ div"),
        panel.get_by_text("List (virtual, grouped)", exact=True).locator(
            "+ div"
        ),
    ]

    for widget, name in zip(
        lists,
        ("Weidner, Ludwig", "Weidner, Ludwig", "Binder, Marita"),
    ):
        item = widget.get_by_text(name, exact=True)
        item.click()
        page.wait_for_timeout(400)
        expect(item.locator("..")).to_have_css(
            "background-color", selected_color
        )


def table_page(page):
    # Table
    page.get_by_role("tab", name="Table", exact=True).click()
    page.wait_for_timeout(400)
    table = page.get_by_role("tabpanel", name="Table").get_by_role("grid")
    rows = table.get_by_role("row")
    row_0, row_1, row_2 = rows.nth(1), rows.nth(2), rows.nth(3)

    row_0.click()
    page.wait_for_timeout(400)
    row_1.click()
    page.wait_for_timeout(400)
    expect(row_1).to_have_css("background-color", selected_color)
    expect(row_0).not_to_have_css("background-color", selected_color)
    expect(row_2).not_to_have_css("background-color", selected_color)

    table.get_by_role("columnheader", name="ID", exact=True).click()
    page.wait_for_timeout(400)
    table.get_by_role(
        "columnheader", name="A number", exact=True
    ).click()
    page.wait_for_timeout(400)


def toolbar_menu_page(page):
    # Toolbar/Menu
    page.get_by_role("tab", name="Toolbar/Menu", exact=True).click()
    page.wait_for_timeout(400)
    panel = page.get_by_role("tabpanel", name="Toolbar/Menu")
    menu_button = panel.get_by_role(
        "button", name="Toolbar MenuButton", exact=True
    )
    menu_button.locator('div[style*="arrows/down.gif"]').click()
    page.wait_for_timeout(400)

    menu_id = menu_button.get_attribute("aria-controls")
    menu = page.locator(f'div[role="menu"].qx-main#{menu_id}')
    menu.get_by_role("menuitem", name="Menu MenuButton", exact=True).click()
    page.wait_for_timeout(400)

    heading = panel.get_by_text("Menu (with slidebar)", exact=True)
    sidebar = heading.locator("..").get_by_role("menu")
    viewport = sidebar.locator('[aria-orientation="vertical"] > div').first
    radio = sidebar.get_by_role(
        "menuitem", name="Menu RadioButton", exact=True
    ).first
    viewport.hover()
    page.mouse.wheel(0, 300)
    page.wait_for_timeout(3000)

    radio.click(force=True)
    expect(radio).to_have_attribute("aria-checked", "true")
    page.wait_for_timeout(400)
    page.get_by_role("tab", name="Window", exact=True).click()
    page.wait_for_timeout(400)


def window_page(page):
    # Window
    panel = page.get_by_role("tabpanel", name="Window")
    panel.get_by_role("tab", name="Page 2", exact=True).click()
    page.wait_for_timeout(400)
    second_window = page.get_by_role("dialog").filter(
        has=page.get_by_text("The second window", exact=True)
    )

    for name in ("Show Close", "Use resize frame", "Movable"):
        checkbox = second_window.get_by_role(
            "checkbox", name=name, exact=True
        )
        checkbox.click()
        page.wait_for_timeout(400)
        expect(checkbox).to_have_attribute("aria-checked", "false")


def tab_page(page):
    # Tab
    page.get_by_role("tab", name="Tab", exact=True).click()
    page.wait_for_timeout(400)
    panel = page.get_by_role("tabpanel", name="Tab")

    top = panel.locator(
        '[role="tablist"]:has([role="tab"].qx-tabview-page-button-top)'
    )
    top.get_by_role("tab", name="Calculator", exact=True).click()
    page.wait_for_timeout(400)

    left = panel.locator(
        '[role="tablist"]:has([role="tab"].qx-tabview-page-button-left)'
    )
    left.get_by_role("tab", name="Calculator", exact=True).click()
    page.wait_for_timeout(400)

    for side in ("bottom", "right"):
        section = panel.locator(
            f'[role="tablist"]:has([role="tab"].qx-tabview-page-button-{side})'
        )
        section.get_by_role("tab", name="Notes", exact=True).click()
        page.wait_for_timeout(400)


def control_page(page):
    # Control
    page.get_by_role("tab", name="Control", exact=True).click()
    page.wait_for_timeout(400)
    panel = page.get_by_role("tabpanel", name="Control")
    panel.locator('[style*="background-color:red"]').click()
    page.wait_for_timeout(400)
    expect(panel.get_by_role("textbox").first).to_have_value("FF0000")
    print("Control: selected the red color preset.")


def embed_page(page):
    # Embed
    page.get_by_role("tab", name="Embed", exact=True).click()
    page.wait_for_timeout(400)
    html = page.get_by_role("tabpanel", name="Embed").locator(
        ".qx-main"
    ).filter(has_text="Lorem ipsum dolor sit amet").last
    html.hover()
    page.mouse.wheel(0, 3000)
    page.wait_for_timeout(400)
    page.mouse.wheel(0, 3000)
    page.wait_for_timeout(400)
    print("Embed: scrolled the HTML text.")


def embed_frame_page(page):
    # EmbedFrame
    page.get_by_role("tab", name="EmbedFrame", exact=True).click()
    page.wait_for_timeout(400)
    frames = page.get_by_role("tabpanel", name="EmbedFrame").locator("iframe")
    for index in range(2):
        frame = frames.nth(index)
        frame.hover(force=True)
        page.mouse.wheel(0, 300)
        page.wait_for_timeout(400)
    expect(frames).to_have_count(2)
    print("EmbedFrame: scrolled over both embedded frames.")


def basic_page(page):
    # Basic
    page.get_by_role("tab", name="Basic", exact=True).click()
    page.wait_for_timeout(400)
    panel = page.get_by_role("tabpanel", name="Basic")
    button = panel.get_by_role("button", name="Disabled")
    button.click()
    page.wait_for_timeout(400)
    expect(button).to_have_attribute("aria-pressed", "true")
    expect(panel.get_by_text("Atom", exact=True)).to_be_visible()
    print("Basic: toggled Disabled and checked the Atom example.")


def misc_page(page):
    # Misc
    page.get_by_role("tab", name="Misc", exact=True).click()
    page.wait_for_timeout(400)
    panel = page.get_by_role("tabpanel", name="Misc")
    for name in ("Item 5", "Item 8"):
        item = panel.get_by_text(name, exact=True)
        item.click()
        page.wait_for_timeout(400)
        expect(item.locator("..")).to_have_css(
            "background-color", selected_color
        )
    print("Misc: selected Item 5 and Item 8.")


def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url, wait_until="domcontentloaded")
        form_page(page)
        tree_page(page)
        list_page(page)
        table_page(page)
        toolbar_menu_page(page)
        window_page(page)
        tab_page(page)
        control_page(page)
        embed_page(page)
        embed_frame_page(page)
        basic_page(page)
        misc_page(page)
        page.wait_for_timeout(4000)
        browser.close()


if __name__ == "__main__":
    main()
