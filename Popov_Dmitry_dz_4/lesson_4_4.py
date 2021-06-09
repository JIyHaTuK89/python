from time import perf_counter
test_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# Множества
# unique_numbers = [el for el in test_list if test_list.count(el) == 1]

# unique_numbers = set()
# tmp = set()
#
# start = perf_counter()
#
# for el in test_list:
#     if el in tmp:
#         unique_numbers.add(el)
#     else:
#         unique_numbers.discard(el)
#     tmp.add(el)
#
# unique_set = tmp - unique_numbers
# unique_set_order = [el for el in test_list if el in unique_set]
# print("Время выполнения {:.8f}".format(perf_counter() - start))
# print(unique_set_order)
# 0.00001140 сек.

# *****************************************************************

num_dict = {}

start = perf_counter()

for el in test_list:
    if el not in num_dict:
        num_dict[el] = 1
    else:
        num_dict[el] += 1

unique_numbers = {el for el in num_dict if num_dict[el] == 1}

# пришлось формат поменять, т.к. выводил число в отрицательной степени
print("Время выполнения {:.8f}".format(perf_counter() - start))

print(list(unique_numbers))
# 0.00000960 сек.
# словарь чуть быстрее, но в первом варианте сохранен порядок чисел

