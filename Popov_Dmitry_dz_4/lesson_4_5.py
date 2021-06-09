# не совсем понял, как именно нужно - сделал 2 варианта
from functools import reduce
from time import perf_counter

test_list = list(range(100, 1001, 2))
print(test_list)
print("-" * 180)


def my_multiple(prev_el, el):
    return prev_el * el


# *********************************************************************************************************************
# второй способ

def foo():
    for i in range(100, 1001, 2):
        yield i


gen = foo()


if __name__ == '__main__':
    start = perf_counter()
    print(reduce(my_multiple, test_list))
    print(f"Время выполнения первого варианта: {perf_counter() - start} сек")
    print("Второй способ " + "-" * 140)
    start = perf_counter()
    print(reduce(lambda a, b: a * b, gen))
    print(f"Время выполнения второго варианта: {perf_counter() - start} сек")
