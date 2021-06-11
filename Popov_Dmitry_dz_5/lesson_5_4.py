# нашел библиотеку перевода, но ее нужно устанавливать через pip, не знаю есть она у вас или нет
# так что буду через словарь выполнять
with open("text_4.txt", "r", encoding="utf-8") as f1, open("new_text_4.txt", "a", encoding="utf-8") as f2:
    translation = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    for string in f1:
        string_as_list = string.split()
        new_string = f'{translation[string_as_list[0]]} '  # f"{translation[string_as_list[0]]} {string_as_list[1]} {string_as_list[2]}
        for el in string_as_list[1:]:
            new_string += f"{el} "
        f2.write(new_string + "\n")

# работает, но кажется, что костыли какие-то я собрал....
# можно было бы так записывать в новый файл так: f"{translation[string_as_list[0]]} {string_as_list[1]} {string_as_list[2]}"
# но если длина строк в дальнейшем будет меняться, то код придется переделывать
# хотя этот код и так дописывать, если числительных будет больше. Тут нужна библиотека переводчик
