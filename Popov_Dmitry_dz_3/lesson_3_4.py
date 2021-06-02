# Сделал как сказано, но мне кажется, что в продакшене вот так не пишут.... Ветвления работают быстрее try-except вроде
def my_func(x, y):
    number = None
    power_number = None
    result = 1
    # Блок валидации x
    try:
        number = float(x)
    except ValueError:
        print('x должно быть числом')
        return

    if number <= 0:
        print('x должен быть больще 0')
        return
    # ------------------------------
    # Блок валидации y
    try:
        power_number = int(y)
    except ValueError:
        print('y должно быть целым числом')
        return
        # ------------------------------
    if power_number >= 0:
        print('y должно быть меньше 0')
    else:
        for _ in range(abs(power_number)):
            result = result / number
    return result


ss = my_func(2, -2)
print(ss)
