import time
import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class BaseActions:

    def __init__(self, url, browser):
        self.url = url
        self.driver = browser

    def open_page(self):
        self.driver.get(self.url)

    def find_element_on_page(self, locator):
        return self.driver.find_element(By.XPATH, locator)

    def click_button(self, locator):
        button = self.find_element_on_page(locator)
        button.click()

    def fill_in_field(self, locator, text):
        field = self.find_element_on_page(locator)
        field.send_keys(text)

    def auth(self, login, password):
        self.click_button(locators.button_signin)
        self.fill_in_field(locators.field_login, login)
        self.fill_in_field(locators.field_password, password)
        self.click_button(locators.button_auth)

    def logout(self):
        self.click_button(locators.account_button)
        self.click_button(locators.exit_button)

    def close_browser(self):
        """Закрывает браузер и завершает работу драйвера."""
        self.driver.quit()

    def fill_big_form(self, form_data: dict):
        for field_name, value in form_data.items():
            try:
                field = self.driver.find_element(By.NAME, field_name)
                if field_name == 'noibiz_avatar' or field_name == 'noibiz_fathername1':
                    continue

                if field_name == "noibiz_gender":
                    select = Select(field)
                    select.select_by_value("m")
                    continue

                field.send_keys(value)
                time.sleep(0.5)
            except Exception as e:
                print(e)
        self.click_button('/html/body/div[3]/form/table/tbody/tr[21]/td[2]/input')

    def find_elements_on_page(self, tag):
        return self.driver.find_elements(By.TAG_NAME, tag)


#def test_1(browser):
#    b = BaseActions('http://users.bugred.ru', browser)
#    b.open_page()
#    
#    #b.find_element_on_page('//*[@id="main-menu"]/ul/li[2]/a/span')
#    b.auth('manager@mail.ru', '1')
#    
#    time.sleep(3)
#    b.click_button(locators.button_add_user)
#    time.sleep(3)
#    b.fill_big_form(form_data)
#    time.sleep(3)
#    #
#    # выход
#    
#    b.logout()
#    #b.click_button(locators.account_button)
#    time.sleep(3)
#    #b.click_button(locators.exit_button)
#    
#    #вход
#    b.auth('ivan@example.com', 'password123')
#    #b.click_button(locators.button_signin)
#    #b.fill_in_field(locators.field_login, 'ivan@example.com')
#    #b.fill_in_field(locators.field_password, 'password123')
#    #b.click_button(locators.button_auth)
#    
#    
#    b.fill_in_field(locators.search_user_field, 'ivan@example.com')
#    time.sleep(2)
#    b.click_button(locators.search_user_button)
#    time.sleep(3)
#    #просмотр элемента
#    
#    b.click_button(locators.view_user_button)
#    time.sleep(2)
#    
#    
#    second_td_values = []
#    rows = b.find_elements_on_page("tr")
#    for row in rows:
#        cells = row.find_elements(By.TAG_NAME, "td")
#        # Если есть хотя бы два <td>, добавляем содержимое второго <td> в список
#        if len(cells) > 1:
#            value = cells[1].text.strip()  # Текст из второго <td>
#            second_td_values.append(value)
#    
#    print(second_td_values)
#    
#    #выход
#    b.logout()
#    #b.click_button(locators.account_button)
#    #b.click_button(locators.exit_button)
#    
#    
#    
#    b.auth('manager@mail.ru', '1')
#    
#    #
#    ## поиск
#    b.fill_in_field(locators.search_user_field, 'ivan@example.com')
#    b.click_button(locators.search_user_button)
#    #
#    #
#    ## удаление
#    b.click_button(locators.delete_user_button)
#    #
#    b.driver.quit()
#    
#    #
#    #
#    #
#    #
#    #