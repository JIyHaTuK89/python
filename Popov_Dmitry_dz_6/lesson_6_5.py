class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Пишем ручкой: {self.title}')


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Пишем карандашом: {self.title}')


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Пишем маркером: {self.title}')


if __name__ == '__main__':
    a = Stationery('Общий')
    a.draw()
    b = Pen('Конспект')
    b.draw()
    c = Pencil('Портрет')
    c.draw()
    d = Handle('Заметки')
    d.draw()
