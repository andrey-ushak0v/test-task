from dataclasses import dataclass


form_data = {
    "noibiz_name": "Ваня",
    "noibiz_email": "ivan@example.com",
    "noibiz_password": "password123",
    "noibiz_avatar": "photo_1.png",
    "noibiz_birthday": "1990-01-01",
    "noibiz_gender": "m",
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


@dataclass
class Credentials:
    manager_login = 'manager@mail.ru'
    manager_password = '1'
    user_login = 'ivan@example.com'
    user_password = 'password123'
