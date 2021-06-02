# в данной реализации код пропускает цифры и знаки типа ! . ,
# если это критично, то просто берем сипсок строчных латинских букв и через if in делаем фильтр
def int_func(word=str(input("Введите слово строчными латинскими буквами: "))):
    """checks if letters are latin, lower case and returns string whith upper case first letters of words"""

    if " " in word:
        words_list = word.split()
        print(words_list)
        for el in words_list:
            for letter in el:
                if ord(letter) in list(range(ord("a"), ord("z"))):
                    return word.title()
                else:
                    print("Вводите только строчные латинские буквы")
                    return
    for letter in word:
        if ord(letter) in list(range(ord("a"), ord("z"))):
            return word.capitalize()
        else:
            print("Вводите только строчные латинские буквы")
            return


filtered = int_func()
print(filtered)
