class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, args):
        return self.browser.find_element(*args)

    def find_a_few_elements(self, args):
        return self.browser.find_elements(*args)
