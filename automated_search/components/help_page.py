from selenium.webdriver.common.by import By
from .base_page import BasePage

checkbox_selector_rolex = (By.XPATH, "//input[@aria-label='Rolex']")
checkbox_selector_casio = (By.XPATH, "//input[@aria-label='Casio']")


class HelpPageSearch(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=watch&_sacat=0')

    def checkbox(self):
        return self.find(checkbox_selector_rolex)

    def checkbox_is_displayed(self):
        return self.checkbox().is_displayed()

    def un_checkbox(self):
        return self.find(checkbox_selector_rolex)

    def checkbox_casio(self):
        return self.find(checkbox_selector_casio)

    def get_first_two_items(self):
        items = self.find_a_few_elements((By.XPATH, "//ul//li[@data-viewport]"))[:2]
        return items

    def get_last_two_items(self):
        items = self.find_a_few_elements((By.XPATH, "//ul//li[@data-viewport][last()-1]"))[:2]
        return items

    @staticmethod
    def get_titles_and_prices(items, prices):
        titles_prices = []
        for item in items, prices:
            title = item.find((By.XPATH, "//ul//span[@role='heading']")).text
            price = item.find((By.XPATH, "//ul//span[@class='s-item__price']")).text
            titles_prices.append((title, price))
            return titles_prices

    @staticmethod
    def verify_items(items, stored_data):
        mismatches = []
        for index, item in enumerate(items):
            title = item.find(".//h3[@class='s-item__title']").text
            price = item.find(".//span[@class='s-item__price']").text
            stored_title, stored_price = stored_data[index]

            if "rolex" not in title.lower() and "rolex" not in stored_title.lower():
                mismatches.append(f"Item {index + 1}: Title mismatch - Expected 'rolex' not found")

            if price != stored_price:
                mismatches.append(f"Item {index + 1}: Price mismatch - Expected: {stored_price}, Actual: {price}")

        if mismatches:
            print("Mismatches:")
            for mismatch in mismatches:
                print(mismatch)
        else:
            print("No mismatches found")

