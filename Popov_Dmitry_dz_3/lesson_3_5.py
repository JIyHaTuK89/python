numbers_list = []
STOP_SCRIPT = "{"

while True:
    ask = input("Введите числа через пробел: ").split()
    if "{" in ask:
        ask.pop()
        try:
            for number in ask:
                numbers_list.append(int(number))
            print(sum(numbers_list))
        except ValueError:
            print("Нужно вводить только числа!")
            break
        break
    try:
        for number in ask:
            numbers_list.append(int(number))
        print(sum(numbers_list))
    except ValueError:
        print("Нужно вводить только числа!")
        break
