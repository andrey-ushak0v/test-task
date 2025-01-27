import locators.user_locators as user_locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from actions.base_actions import BaseActions


class UserActions(BaseActions):
    url = 'http://users.bugred.ru'

    def auth(self, login, password):
        self.click_button(user_locators.button_signin)
        self.fill_in_field(user_locators.field_login, login)
        self.fill_in_field(user_locators.field_password, password)
        self.click_button(user_locators.button_auth)

    def logout(self):
        self.click_button(user_locators.account_button)
        self.click_button(user_locators.exit_button)

    def fill_big_form(self, form_data: dict):
        for field_name, value in form_data.items():

            field = self.find_element_on_page_by_name(field_name)
            if field_name == 'noibiz_avatar':
                continue

            if field_name == "noibiz_gender":
                select = Select(field)
                select.select_by_value("m")
                continue

            if field_name == 'noibiz_fathername1':
                field = self.find_element_on_page_by_xpath(
                    user_locators.fathername_field
                    )
            field.send_keys(value)

        self.click_button('/html/body/div[3]/form/table/tbody/tr[21]/td[2]/input')

    def get_form_data(self):
        second_td_values = []
        rows = self.find_elements_on_page_by_tag('tr')
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            if len(cells) > 1:
                if cells[0].text.strip() == 'Пол':
                    value = cells[1].find_element(By.CSS_SELECTOR, "option[selected]").text.strip()
                else:
                    value = cells[1].text.strip()
                second_td_values.append(value)

        return second_td_values
