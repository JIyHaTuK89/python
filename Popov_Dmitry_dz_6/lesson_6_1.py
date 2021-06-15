from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = None

    # здесь я добавил print'ы просто для наглядности, хотя в условии не требовалось
    # yield для использования цикла при проверке последовательности, метод генераторный
    def running(self):
        self.__color = "Красный"
        print(self.__color)
        yield self.__color
        sleep(7)
        self.__color = "Жёлтый"
        print(self.__color)
        yield self.__color
        sleep(2)
        self.__color = "Зелёный"
        print(self.__color)
        yield self.__color
        sleep(5)


if __name__ == "__main__":
    traffic_light = TrafficLight()

    light_order = []

    # т.к. метод реализован как генератор, его можно использовать в цикле for-in
    for light in traffic_light.running():
        light_order.append(light)

    assert (light_order == ["Красный", "Жёлтый", "Зелёный"]), "Светофор неисправен"
