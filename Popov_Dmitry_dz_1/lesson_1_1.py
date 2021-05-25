# Поработайте с переменными, создайте несколько, выведите на экран. Запросите у пользователя некоторые числа и строки
# и сохраните в переменные, затем выведите на экран.

variable_int = 50
variable_float = 12.5
variable_str = "letters"
variable_bool = True

print(f"целочисленное число: {variable_int}, тип: {type(variable_int)}")
print(f"дробное число: {variable_float}, тип: {type(variable_float)}")
print(f"строка: {variable_str}, тип: {type(variable_str)}")
print(f"булевое: {variable_bool}, тип: {type(variable_bool)}")

print("-" * 50)

first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

print(f"Вы ввели числа: {first_number} и {second_number}")

print("-" * 50)

first_word = input("Введите первое слово: ")
second_word = input("Введите второе слово: ")

print(f"Вы ввели слова: {first_word} и {second_word}")
