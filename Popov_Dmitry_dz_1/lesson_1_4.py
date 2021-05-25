# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

while True:
    user_nimber = int(input("Введите число: "))
    if user_nimber <= 0:
        continue
    else:
        break

max_value = -1

while user_nimber > 10:
    d = user_nimber % 10
    user_nimber //= 10
    if d > max_value:
        max_value = d

print(f"Максимальная цифра вашего числа: {max_value}")
