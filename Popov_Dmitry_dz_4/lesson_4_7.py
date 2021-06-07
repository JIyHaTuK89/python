def fact(n):
    result = 1
    for number in range(1, n + 1):
        yield number
        result *= number

print(fact(4)) # проверка возвращаемого объекта

# здесь не понял, если только первые n числа то есть без последнего? Тогда там if el != 4: дописать нужно
# либо в самой функции добавить if number != n
for el in fact(4):
    print(el)
