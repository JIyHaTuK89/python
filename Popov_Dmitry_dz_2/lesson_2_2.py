# Можно реализовать через цикл while и поочереди аппендить эелементы в пустой список,
# пока пользователь не введет команду которая вызовет break в цикле(либо регулировать длинну списка,
# заранее спросив желаемую длину списка и поместить в счетчик цикла),
# но мне показалось это неуклюжей реализацией.
# ---------------------------------------------------------------------------------------------------------------------
user_list = input("Введите эелементы через запятую, БЕЗ ПРОБЕЛОВ: ").split(",")
print(f"Ваш список: {user_list}")
# хотя и в этом решении есть недостаток, если у пользователя есть запятые в самих элементах.
# С пробелами тоже могут быть проблемы.
# Тут уже нужно смотреть по проекту в целом (что требуется вносить в список)
# ----------------------------------------------------------------------------------------------------------------------
if len(user_list) % 2:
    last_el = user_list.pop()
    j = 0
    for i in range(int(len(user_list) / 2)):
        user_list[j], user_list[j + 1] = user_list[j + 1], user_list[j]
        j += 2
    user_list.append(last_el)
    print(f"Ваш измененный список: {user_list}")
else:
    j = 0
    for i in range(int(len(user_list) / 2)):
        user_list[j], user_list[j + 1] = user_list[j + 1], user_list[j]
        j += 2
    print(f"Ваш измененный список: {user_list}")