from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseActions:
    url = None

    def __init__(self, browser):
        self.driver = browser

    def open_page(self):
        self.driver.get(self.url)

    def find_element_on_page_by_xpath(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )

    def find_element_on_page_by_name(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.NAME, locator))
        )

    def click_button(self, locator, timeout=5):
        button = self.find_element_on_page_by_xpath(locator, timeout)
        button.click()

    def fill_in_field(self, locator, text, timeout=5):
        field = self.find_element_on_page_by_xpath(locator, timeout)
        field.send_keys(text)

    def close_browser(self):
        self.driver.quit()

    def find_elements_on_page_by_tag(self, tag, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, tag))
        )
