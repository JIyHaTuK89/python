with open("text_5.txt", "w+", encoding="utf-8") as f:
    new_string = input("Введите числа через пробел: ")
    f.write(new_string)
    f.seek(0)
    file_numbers = f.read().split()
    numbers_sum = sum(list(map(float, file_numbers)))
    print(numbers_sum)