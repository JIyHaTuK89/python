# здесь не стал использовать try-except для валидации аргументов т.к. не требовалось по заданию да и это элементарно
from itertools import cycle, count


def num_generator(start, step):
    for number in count(start, step):
        if number > start * 100:
            break
        else:
            yield number


def repeat_elements(list, repeats):
    for el in cycle(list):
        if repeats == 0:
            break
        else:
            repeats -= 1
            yield el


if __name__ == '__main__':
    result = num_generator(3, 3)
    print(list(result))
    result_2 = repeat_elements("ABC", 10)
    print(list(result_2))
