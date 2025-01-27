import locators.user_locators as user_locators
from actions.user_actions import UserActions
from utils.user_data import form_data


def test_user_data_in_account(browser):
    b = UserActions(browser)
    b.open_page()

    b.auth('manager@mail.ru', '1')
    b.click_button(user_locators.button_add_user)
    b.fill_big_form(form_data)
    b.logout()

    b.auth('ivan@example.com', 'password123')
    b.fill_in_field(user_locators.search_user_field, 'ivan@example.com')
    b.click_button(user_locators.search_user_button)
    b.click_button(user_locators.view_user_button)
    user_data = b.get_form_data()
    b.logout()

    b.auth('manager@mail.ru', '1')
    b.fill_in_field(user_locators.search_user_field, 'ivan@example.com')
    b.click_button(user_locators.search_user_button)
    b.click_button(user_locators.delete_user_button)
    b.driver.quit()
    print(user_data)
    print(list(form_data.values()))
    assert user_data == list(form_data.values())
