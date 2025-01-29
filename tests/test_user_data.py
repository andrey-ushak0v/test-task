from locators.user_locators import UserLocstors
from actions.user_actions import UserActions
from utils.error_messages import message_test_user_data_in_account
from utils.user_data import form_data, Credentials
import pytest


class TestUserData:

    @pytest.fixture(autouse=True)
    def open_page(self, browser):
        self.app = UserActions(browser)
        self.app.open_page()

    def test_user_data_in_account(self):
        """Тест на проверку совпадения данных,
           введенных при создании пользователя
           и данных отображающихся в аккаунте.

           Шаги:
           1) Залогиниться од менеджером
           2) Создать нового пользователя, заполнив все поля.
           3) Выйти из аккаунта менеджера
           4) Залогиниться новым пользователем
           5) В списке пользователей найти пользователя поиском и нажать на нем кнопку Посмотреть
           6) Сравнить те поля, что тут отображаются, с введенными при создании
           7) Залогиниться менеджером
           8) Найти пользователя поиском и удалить его
           """
        self.app.auth(Credentials.manager_login, Credentials.manager_password)
        self.app.click_button(UserLocstors.button_add_user)
        self.app.fill_user_form(form_data)
        self.app.logout()

        self.app.auth(Credentials.user_login, Credentials.user_password)
        self.app.fill_in_field(UserLocstors.search_user_field, Credentials.user_login)
        self.app.click_button(UserLocstors.search_user_button)
        self.app.click_button(UserLocstors.view_user_button)
        user_data = self.app.get_form_data()
        assert user_data == list(form_data.values()), message_test_user_data_in_account
        self.app.logout()

        self.app.auth(Credentials.manager_login, Credentials.manager_password)
        self.app.fill_in_field(UserLocstors.search_user_field, Credentials.user_login)
        self.app.click_button(UserLocstors.search_user_button)
        self.app.click_button(UserLocstors.delete_user_button)

       
