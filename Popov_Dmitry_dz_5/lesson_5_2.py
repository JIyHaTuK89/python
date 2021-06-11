# напишите, пожалуйста, стоило ли так расписывать и думать о производительности или я вообще тут создал много лишних шагов?
# это можно сократить, но мне кажется такой вариант изящнее. Не совсем разобрался еще как принято в производстве
with open("text_2.txt", "r", encoding="utf-8") as f:
    data_dict = {}  # словарь номеров строк и кол-ва слов в них
    strip_number = 0
    for string in f:
        strip_number += 1
        words_amount = string.split()
        data_dict[strip_number] = len(words_amount)
    for item in data_dict.items():
        print(f"В {item[0]}-й строке {item[1]} слов(а)")
    print(f"Всего строк: {strip_number}")
