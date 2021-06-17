class Cell:

    def __init__(self, sub_cell_count):
        self.sub_cell_count = sub_cell_count

    def __str__(self):
        return f'клетка содержет {self.sub_cell_count} ячеек'

    def __repr__(self):
        return 'Cell({})'.format(self.sub_cell_count)

    def __add__(self, other):
        return Cell(self.sub_cell_count + other.sub_cell_count)

    def __sub__(self, other):
        if self.sub_cell_count > other.sub_cell_count:
            return Cell(self.sub_cell_count - other.sub_cell_count)
        else:
            print('Количество ячеек первого операнда должно привышать количесво ячеек второго')

    def __mul__(self, other):
        return Cell(self.sub_cell_count * other.sub_cell_count)

    def __truediv__(self, other):
        return Cell(self.sub_cell_count // other.sub_cell_count)

    def __floordiv__(self, other):
        return Cell(self.sub_cell_count // other.sub_cell_count)

    def make_order(self, line_length):
        _full_lines_count = self.sub_cell_count // line_length
        _tail = self.sub_cell_count - (line_length * _full_lines_count)
        _line_example = f'{"*" * line_length}\n'
        _tail_example = f'{"*" * _tail}'
        return f'{_line_example * _full_lines_count + _tail_example}'


if __name__ == '__main__':
    a = Cell(6)
    b = Cell(8)
    print(b - a)
    print(a + b)
    print(a * b)
    print(b / a)
    print(repr(b.make_order(5)))