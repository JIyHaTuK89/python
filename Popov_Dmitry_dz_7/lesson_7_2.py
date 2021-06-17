from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def calculate_fabric_consumtion(self):
        pass

class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def calculate_fabric_consumtion(self):
        return self.v / 6.5 + 0.5

class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def calculate_fabric_consumtion(self):
        return self.h * 2 + 0.3

if __name__ == "__main__":
    c = Coat(30)
    print(round(c.calculate_fabric_consumtion, 2))

    s = Suit(150)
    print(s.calculate_fabric_consumtion)