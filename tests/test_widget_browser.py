from pages.basic_page import BasicPage
from pages.control_page import ControlPage
from pages.embed_frame_page import EmbedFramePage
from pages.embed_page import EmbedPage
from pages.form_page import FormPage
from pages.list_page import ListPage
from pages.misc_page import MiscPage
from pages.tab_page import TabPage
from pages.table_page import TablePage
from pages.toolbar_menu_page import ToolbarMenuPage
from pages.tree_page import TreePage
from pages.widget_browser_page import WidgetBrowserPage
from pages.window_page import WindowPage


def test_widget_browser_demos(page):
    widget_browser = WidgetBrowserPage(page)
    widget_browser.open()

    form_page = FormPage(page)
    form_page.fill_name()
    form_page.fill_password()
    form_page.select_combo_box_item_9()
    form_page.select_virtual_combo_box_item_299()

    widget_browser.navigate_to_demo("Tree")
    TreePage(page).select_tree_and_virtual_tree_items()

    widget_browser.navigate_to_demo("List")
    ListPage(page).select_list_items()

    widget_browser.navigate_to_demo("Table")
    TablePage(page).select_rows_and_sort_columns()

    widget_browser.navigate_to_demo("Toolbar/Menu")
    ToolbarMenuPage(page).use_toolbar_and_sidebar_menus()

    WindowPage(page).change_second_window_options()

    widget_browser.navigate_to_demo("Tab")
    TabPage(page).select_calculator_and_notes_tabs()

    widget_browser.navigate_to_demo("Control")
    ControlPage(page).select_red_color()

    widget_browser.navigate_to_demo("Embed")
    EmbedPage(page).scroll_embedded_content()

    widget_browser.navigate_to_demo("EmbedFrame")
    EmbedFramePage(page).scroll_embedded_frames()

    widget_browser.navigate_to_demo("Basic")
    BasicPage(page).toggle_disabled_and_check_atom()

    widget_browser.navigate_to_demo("Misc")
    MiscPage(page).select_items()

    page.wait_for_timeout(4000)
