# Не стал реализовывать в принтах гражданский/полицейский.
# Ничего сложного, проверка параметра на true/false и добавление в принт, но код и без того длинный
class Car:

    def __init__(self, name, color, speed=None, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self, speed=30):
        self.speed = speed
        print(f'{self.color} {self.name} начинаем движение со скоростью скорость {speed} км/ч.')

    def stop(self):
        print(f'{self.color} {self.name} остановился')

    def turn(self, where=None):
        self.where = where
        if where == None:
            print(f'{self.color} {self.name} свернул')
        elif where == 'right':
            print(f'{self.color} {self.name} свернул направо')
        elif where == 'left':
            print(f'{self.color} {self.name} свернул налево')
        elif where == 'back':
            print(f'{self.color} {self.name} сдает назад')
        else:
            print('Вы должны указать направление: right, left, back')

    def show_speed(self):
        speed = self.speed
        if self.speed == None:
            print('Вам сперва нужно начать движение. Воспользуйтесь методом ".go()"')
        print(f'Скорость {self.color} {self.name}: {speed} км/ч')


# -------------------------------------------------------------------------------------------------------------

class TownCar(Car):

    def __init__(self, name, color, speed=None, is_police=False):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        speed = self.speed
        if self.speed == None:
            print('Вам сперва нужно начать движение. Воспользуйтесь методом ".go()"')
        elif self.speed > 40:
            print(f'Вы превысили скорость. Максимально допустимая для грузового автомобиля скорость: 40км/ч')
        else:
            print(f'Скорость {self.color} {self.name}: {speed} км/ч')


# --------------------------------------------------------------------------------------------------------------

class WorkCar(Car):

    def __init__(self, name, color, speed=None, is_police=False):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        speed = self.speed
        if self.speed == None:
            print('Вам сперва нужно начать движение. Воспользуйтесь методом ".go()"')
        elif self.speed > 40:
            print(f'Вы превысили скорость. Максимально допустимая для грузового автомобиля скорость: 40км/ч')
        else:
            print(f'Скорость {self.color} {self.name}: {speed} км/ч')


# ---------------------------------------------------------------------------------------------------------------

class SportCar(Car):

    def __init__(self, name, color, speed=None, is_police=False):
        super().__init__(name, color, speed, is_police)


# ---------------------------------------------------------------------------------------------------------------

class PoliceCar(Car):

    def __init__(self, name, color, speed=None, is_police=True):
        super().__init__(name, color, speed, is_police)


if __name__ == '__main__':
    a = WorkCar('Камаз', 'Зеленый')
    a.show_speed()
    a.go(65)
    a.show_speed()
    a.stop()
    a.go(35)
    a.show_speed()
    a.turn()
    a.turn('right')
