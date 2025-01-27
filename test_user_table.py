import locators
from main import BaseActions
import time
from selenium.webdriver.common.by import By


form_data = {
    "noibiz_name": "Ваня",
    "noibiz_email": "ivan@example.com",
    "noibiz_password": "password123",
    "noibiz_avatar": "path_to_avatar.jpg",  # Путь к файлу для загрузки
    "noibiz_birthday": "1990-01-01",
    "noibiz_gender": "m",  # Мужской
    "noibiz_date_start": "2020-01-01",
    "noibiz_hobby": "Футбол",
    "noibiz_name1": "Иван",
    "noibiz_surname1": "Иванов",
    "noibiz_fathername1": "Иванович",
    "noibiz_cat": "Мурка",
    "noibiz_dog": "Шерлок",
    "noibiz_parrot": "Полли",
    "noibiz_cavy": "Петя",
    "noibiz_hamster": "Бобик",
    "noibiz_squirrel": "Белочка",
    "noibiz_phone": "1234567890",
    "noibiz_adres": "Москва, ул. Ленина, д. 1",
    "noibiz_inn": "123456789012"
}


def test_1(browser):
    b = BaseActions('http://users.bugred.ru', browser) 
    b.open_page()                                       
    b.auth('manager@mail.ru', '1')
    b.click_button(locators.button_add_user)
    b.fill_big_form(form_data)
    b.logout()

    b.auth('ivan@example.com', 'password123')
    b.fill_in_field(locators.search_user_field, 'ivan@example.com')
    b.click_button(locators.search_user_button)
    b.click_button(locators.view_user_button)

    second_td_values = []
    rows = b.find_elements_on_page("tr")
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        # Если есть хотя бы два <td>, добавляем содержимое второго <td> в список
        if len(cells) > 1:
            if cells[0].text.strip() == 'Пол':
                value = cells[1].find_element(By.CSS_SELECTOR, "option[selected]").text.strip()
            else:
                value = cells[1].text.strip()  # Текст из второго <td>
            second_td_values.append(value)

    print(second_td_values)
    b.logout()

    b.auth('manager@mail.ru', '1')
    b.fill_in_field(locators.search_user_field, 'ivan@example.com')
    b.click_button(locators.search_user_button)
    b.click_button(locators.delete_user_button)
  
    b.driver.quit()
    