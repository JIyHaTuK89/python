# имя, фамилия, год рождения, город проживания, email, телефон
def personal_data(name=None, surname=None, birth_date=None, city=None, email=None, phone_number=None):
    return f"Клиент {name} {surname}, {birth_date} года рождения, проживает в городе {city}." \
           f" Контактные данные: Email: {email}, номер телефона: {phone_number}"


first_person = personal_data(name="Дмитрий", surname="Попов", birth_date="12.02.1989",
                             city="Пенза", email="Som89@yandex.ru", phone_number=+79674442233)
print(first_person)
