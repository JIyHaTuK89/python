class Road:
    THICKNESS_CM = 5
    SQUARE_METER_MASS = 25  # исходя из 1см на килограм

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_mass(self):
        return self._length * self._width * self.SQUARE_METER_MASS * self.THICKNESS_CM


if __name__ == "__main__":
    road = Road(5000, 20)
    print(f"{road.calculate_mass() / 1000} тонн")
