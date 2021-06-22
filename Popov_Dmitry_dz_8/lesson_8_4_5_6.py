# методы move_to и transfere сначала были прописаны в каждом классе printer, xerox, scaner, поэтому 160 строк было
# перенес в родительский класс, все работает, но синтаксис подсвечен...
class Warehouse:
    company_branches = {}

    def __init__(self, branch_name):
        self.branch_name = branch_name
        Warehouse.company_branches[self.branch_name] = {}

    def __str__(self):
        return Warehouse.company_branches


class Office_equipment:

    def __init__(self, maker):
        self.maker = maker

    def __str__(self):
        return f'{self.maker}'

    def move_to(self, branch, amount):
        self.branch = branch
        self.count = amount
        try:
            if isinstance(amount, str):
                raise TypeError('Нужно ввести целочисленное число')
        except TypeError as err:
            print(err)
        if Warehouse.company_branches[branch].get(f"{self.maker}, {self.types}") is None: #ошибка доработать
            Warehouse.company_branches[branch][f"{self.maker}, {self.types}"] = amount
        elif Warehouse.company_branches[branch].get(f"{self.maker}, {self.types}"):
            Warehouse.company_branches[branch][f"{self.maker}, {self.types}"] += amount

    def transfere(self, from_where, to_where, amount):
        self.from_where = from_where
        self.to_where = to_where
        self.amount = amount
        try:
            if isinstance(amount, str):
                raise TypeError('Нужно ввести целочисленное число')
        except TypeError as err:
            print(err)
        if Warehouse.company_branches.get(from_where) is None:
            print('Такого филиала еще не существует')
        elif Warehouse.company_branches[from_where].get(f"{self.maker}, {self.types}") is None:
            print('Такого товара на складе нет')
        elif Warehouse.company_branches[from_where].get(f"{self.maker}, {self.types}") == 0:
            print('Вывозить нечего, ноль единиц товара')
        elif Warehouse.company_branches[from_where].get(f"{self.maker}, {self.types}") < amount:
            print(
                f'Столько товара на складе нет. Остаток: {Warehouse.company_branches[from_where].get(f"{self.maker}, {self.types}")}')
        elif Warehouse.company_branches.get(to_where) is None:
            print('Такого филиала еще не существует')
        elif Warehouse.company_branches[from_where].get(f"{self.maker}, {self.types}"):
            self.equipment_remains = Warehouse.company_branches[from_where][f"{self.maker}, {self.types}"]
            print(self.equipment_remains)
            Warehouse.company_branches[from_where][f"{self.maker}, {self.types}"] = self.equipment_remains - amount
            Warehouse.company_branches[to_where][f"{self.maker}, {self.types}"] += amount


class Printer(Office_equipment):

    def __init__(self, maker, types):
        super().__init__(maker)
        self.types = types

    def __str__(self):
        return f'{self.maker}, {self.types}'


class Scaner(Office_equipment):

    def __init__(self, maker, types):
        super().__init__(maker)
        self.types = types

    def __str__(self):
        return f'{self.maker}, {self.types}'


class Xerox(Office_equipment):

    def __init__(self, maker, types):
        super().__init__(maker)
        self.types = types

    def __str__(self):
        return f'{self.maker}, {self.types}'


if __name__ == '__main__':
    a = Warehouse('Moscow')
    pr = Printer('Canon', 'Laser')
    print(pr)
    pr.move_to('Moscow', 22)
    fg = Printer('Canon', 'Laser')
    pr.move_to('Moscow', 10)
    b = Warehouse('Penza')
    pr2 = Printer('Canon', 'Laser')
    pr2.move_to('Penza', 15)
    print(Warehouse.company_branches)
    pr2.transfere('Moscow', 'Penza', 5)
    print(Warehouse.company_branches)