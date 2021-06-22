class OwnError(Exception):

    def __init__(self, txt):
        self.txt = txt


divisible = input('Введите делимое: ')
divisor = input('Введите делитель: ')

try:
    divisible, divisor = int(divisible), int(divisor)
    if divisor == 0:
        raise OwnError('Делитель не дожен равняться нулю.')
except ValueError:
    print('Вы ввели не число.')
except OwnError as err:
    print(err)
else:
    result = divisible / divisor
    print(f'{divisible} / {divisor} = {result}')


if __name__ == '__main__':
    pass