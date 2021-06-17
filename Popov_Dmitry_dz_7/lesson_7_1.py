class Matrix:

    def __init__(self, list):
        self.list = list

    def __str__(self):
        _matrix = ''
        for el in self.list:
            matrix_line = ' '.join(str(x) for x in el)
            _matrix += f'{matrix_line}\n'
        return _matrix

    def __add__(self, other):
        sum_list = []
        for _list, _list_2 in zip(self.list, other.list):
            sub_list = []
            for num, num_2 in zip(_list, _list_2):
                sub_list.append(num + num_2)
            sum_list.append(sub_list)
        return Matrix(sum_list)


if __name__ == '__main__':
    list_1 = [[23, 53, 17], [4, -8, 36]]
    list_2 = [[13, 33, 7], [12, -8, 86]]
    matrix_1 = Matrix(list_1)
    print(f'Из списка list_1 получили матрицу:\n{matrix_1}')
    matrix_2 = Matrix(list_2)
    sum_matrix = matrix_1 + matrix_2
    print(f'Сложив два списка, получили матрицу:\n{sum_matrix}')