# жаль нельзя пользоваться регулярками (((
with open("text_6.txt", "r", encoding="utf-8") as f:
    subjects_info = {}
    for string in f:
        numbers = []
        string_as_list = string.split()
        for el in string_as_list[1:]:
            if el == "-":
                continue
            else:
                amount = el.split("(")
                numbers.append(int(amount[0]))
            subject = string_as_list[0].split(":")[0]
            subjects_info[subject] = sum(numbers)
    print(subjects_info)

