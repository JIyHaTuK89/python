user_list = input("Введите слова через пробел: ").split()
for el in enumerate(user_list, 1):
    print(el[0], el[1][:10])