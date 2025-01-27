from selenium.webdriver.common.by import By


class BaseActions:
    url = None

    def __init__(self, browser):
        self.driver = browser

    def open_page(self):
        self.driver.get(self.url)

    def find_element_on_page_by_xpath(self, locator):
        return self.driver.find_element(By.XPATH, locator)

    def find_element_on_page_by_name(self, locator):
        return self.driver.find_element(By.NAME, locator)

    def click_button(self, locator):
        button = self.find_element_on_page_by_xpath(locator)
        button.click()

    def fill_in_field(self, locator, text):
        field = self.find_element_on_page_by_xpath(locator)
        field.send_keys(text)

    def close_browser(self):
        self.driver.quit()

    def find_elements_on_page_by_tag(self, tag):
        return self.driver.find_elements(By.TAG_NAME, tag)
