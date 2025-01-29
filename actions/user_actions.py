from locators.user_locators import UserLocstors
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from actions.base_actions import BaseActions
import os


class UserActions(BaseActions):
    url = 'http://users.bugred.ru'

    def auth(self, login, password):
        self.click_button(UserLocstors.button_signin)
        self.fill_in_field(UserLocstors.field_login, login)
        self.fill_in_field(UserLocstors.field_password, password)
        self.click_button(UserLocstors.button_auth)

    def logout(self):
        self.click_button(UserLocstors.account_button)
        self.click_button(UserLocstors.exit_button)

    def fill_user_form(self, form_data: dict):
        for field_name, value in form_data.items():

            field = self.find_element_on_page_by_name(field_name)
            if field_name == 'noibiz_avatar':
                field.send_keys(f'{os.getcwd()}/utils/test_photos/photo_1.png')
                continue

            if field_name == "noibiz_gender":
                select = Select(field)
                select.select_by_value("m")
                continue

            if field_name == 'noibiz_fathername1':
                field = self.find_element_on_page_by_xpath(
                    UserLocstors.fathername_field
                    ) 
            field.send_keys(value)
        self.click_button(UserLocstors.button_submit_new_user)

    def get_form_data(self):
        user_data_from_account = []
        rows = self.find_elements_on_page_by_tag('tr')
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            if len(cells) > 1:
                if cells[0].text.strip() == 'Пол':
                    value = cells[1].find_element(By.CSS_SELECTOR, "option[selected]").text.strip()
                else:
                    value = cells[1].text.strip()
                user_data_from_account.append(value)

        return user_data_from_account
