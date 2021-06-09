# result = [x for x in range(20, 241) if x % 20 == 0 or x % 21 == 0]
# функкцию написал потренироваться

def true_div(start, stop, divisible_1, divisible_2):
    """ function finds all numbers that divisible with two numbers
        and returns generator object

    :param start: first number in range
    :param stop: last number in range
    :param divisible_1: number
    :param divisible_2: number
    :return: generator object
    """
    try:
        return [x for x in range(start, stop + 1) if x % divisible_1 == 0 or x % divisible_2 == 0]
    except ZeroDivisionError:
        print("Ошибка деления на ноль, проверьте вводимые данные")
    except ValueError:
        print("Вводите только числа")


if __name__ == '__main__':
    # print(list(result))
    print(list(true_div(20, 240, 20, 21)))
