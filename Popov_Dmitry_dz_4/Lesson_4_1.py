from sys import argv


def calculate_salary():
    production, rate_per_hour, bonus = argv[1:]
    try:
        total_salary = float(production) * float(rate_per_hour) + float(
            bonus)  # использовал float, т.к. скорее всего будут дробные числа в суммах
        return total_salary
    except ValueError:
        print("Вводите только числа")


# этот блок буду теперь везде писать, просто что б в привычку вошел
if __name__ == '__main__':
    _test = calculate_salary()
    print(_test)
