from selenium.webdriver.common.by import By
from components.help_page import HelpPageSearch


def test_rolex(browser):
    left_filter_pane = HelpPageSearch(browser)
    left_filter_pane.open()
    left_filter_pane.checkbox().click()
    rolex_items = HelpPageSearch(browser)
    rolex_items.get_first_two_items()
    rolex_titles_prices = HelpPageSearch
    rolex_titles_prices.get_titles_and_prices(rolex_items, rolex_titles_prices)
    verify_items = HelpPageSearch(browser)
    verify_items.get_titles_and_prices(rolex_items, rolex_titles_prices)
    left_filter_pane.un_checkbox().click()
    left_filter_pane.checkbox_casio().click()
    casio_items = HelpPageSearch(browser)
    casio_items.get_last_two_items()
    casio_titles_prices = HelpPageSearch(browser)
    casio_titles_prices.get_titles_and_prices(casio_items, casio_titles_prices)
    verify_items = HelpPageSearch(browser)
    verify_items.get_titles_and_prices(casio_items, casio_titles_prices)
