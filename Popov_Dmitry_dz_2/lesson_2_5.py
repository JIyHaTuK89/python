my_list = [7, 5, 3, 3, 2]

user_number = int(input("Введите целочисленное число: "))

if user_number in my_list:
    same_el_amount = my_list.count(user_number)
    el_idx = my_list.index(user_number)
    my_list.insert(el_idx + same_el_amount, user_number)
elif user_number < my_list[-1]:
    my_list.append(user_number)
elif user_number not in my_list:
    i = 0  # переменная-счетчик
    for el in my_list:
        if el > user_number:
            i += 1
        elif el < user_number:
            my_list.insert(i, user_number)
            break

print(my_list)
