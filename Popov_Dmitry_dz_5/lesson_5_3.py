with open("text_3.txt", "r", encoding="utf-8") as f:
    data_dict = {}
    less_then_20000 = []
    person_number = 0
    for string in f:
        person_number += 1
        string_as_list = string.split()
        name, salary = string_as_list[0], float(string_as_list[1])
        data_dict[name] = salary
        if salary < 20000:
            less_then_20000.append(name)
    total_salary = 0
    for val in data_dict.values():
        total_salary += val
    average_salary = total_salary / person_number
    print(f"Сотрудники с окладом менее 20000: {less_then_20000}\nСредний оклад сотрудников: {average_salary}")
