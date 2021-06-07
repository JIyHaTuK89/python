test_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def sort_numbers(some_list):
    comparing_gen = []
    for number in range(1, len(some_list)):
        comparing_gen = [some_list[idx] for idx in range(1, len(some_list)) if some_list[idx] > some_list[idx - 1]]
    return comparing_gen


# Более читабельный вариант
# def sort_numbers(sorting_list):
#     resault_list = []
#     for number in range(1, len(sorting_list)):
#         if int(sorting_list[number]) > int(sorting_list[number - 1]):
#             resault_list.append(sorting_list[number])
#     return resault_list

if __name__ == '__main__':
    print(sort_numbers(test_list))
