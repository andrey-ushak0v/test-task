from dataclasses import dataclass


@dataclass
class UserLocstors:
    button_signin = '//span[contains(text(), "Войти")]'
    field_login = '//input[@name="login"]'
    field_password = '//input[@type="password"]'
    button_auth = '//input[@value="Авторизоваться"]'
    button_add_user = '//a[contains(text(), "Добавить пользователя")]'
    button_submit_form_user = '//input[@name="act_create"]'
    account_button = '//*[@id="fat-menu"]/a'
    exit_button = '//a[text()="Выход"]'
    search_user_field = '//input[@type="text"]'
    button_user_list = '//span[text()="Пользователи"]'
    search_user_button = '//button[contains(text(), "Найти")]'
    view_user_button = '//a[contains(text(), "Посмотреть")]'
    delete_user_button = '//a[contains(text(), "Удалить")]'
    fathername_field = '//input[@data-myname="noibiz_fathername1"]'
    button_submit_new_user = '//input[@value="Добавить пользователя"]'
