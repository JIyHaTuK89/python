def division_num(a, b):
    """returns result og division a and b

    :param a: number
    :param b: number
    :return: number
    """
    try:
        result = a // b
        return result
    except ZeroDivisionError:
        print("Делить на ноль нельзя!")


div_result = division_num(20, 0)

print(div_result)
