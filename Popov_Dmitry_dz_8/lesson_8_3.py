import re

class InvalError(Exception):

    def __init__(self, txt):
        self.txt = txt

numbers_list = []

while True:
    user_input = input('Введите: ')
    if user_input == 'stop'.lower():
        print(numbers_list)
        break
    try:
        if not re.match('(?:[\d.]+)', user_input):
            raise InvalError('Вводите числа!')
    except InvalError as err:
        print(err)
    else:
        numbers_list += numbers_list.append(user_input)
    finally:
        continue

if __name__ == '__main__':
    pass