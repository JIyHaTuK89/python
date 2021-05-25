# Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_number = int(input("Введите количество секунд, которые вам необходимо конвертировать в д:чч:мм:сс: "))

days = ((user_number // 60) // 60) // 24
hours = (user_number - (days * 24 * 60 * 60)) // 60 // 60
minutes = (user_number - (((hours * 60 * 60) + (days * 24 * 60 * 60)))) // 60
seconds = user_number - ((minutes * 60) + (hours * 60 * 60) + (days * 24 * 60 * 60))

print(f"{user_number} сек = {days} д. {hours:02d} ч. {minutes:02d} мин. {seconds:02d} сек.")
