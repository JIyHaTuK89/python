#Честно, я не понял что именно должно быть, как и не знаю толком что такое комплексные числа, нашел только формулы их арифметических операций
class ComlexNum:

    def __init__(self, real_num, imaginary_num):
        self.real_num = real_num
        self.imaginary_num = imaginary_num

    def __str__(self):
        return f'{self.real_num:}{self.imaginary_num:+}j'

    def __add__(self, other):
        return ComlexNum(self.real_num + other.real_num, self.imaginary_num + other.imaginary_num)

    def __sub__(self, other):
        return ComlexNum(self.real_num - other.real_num, self.imaginary_num - other.imaginary_num)

    def __mul__(self, other):
        self.real_mul = self.real_num * other.real_num - self.imaginary_num * other.imaginary_num
        self.imagin_mul = self.real_num * other.imaginary_num + self.imaginary_num * other.real_num
        return ComlexNum(self.real_mul, self.imagin_mul)

    def __truediv__(self, other):
        # в делении не стал округлять, явно не требуется, но возможно требуется полное значение
        self.real_div = (self.real_num * other.real_num - self.imaginary_num * other.imaginary_num) / (other.real_num**2 + other.imaginary_num**2)
        self.imagin_div = (other.real_num * self.imaginary_num - self.real_num * other.imaginary_num) / (other.real_num**2 + other.imaginary_num**2)
        return ComlexNum(self.real_div, self.imagin_div)

if __name__ == '__main__':
    a = ComlexNum(4, 2)
    b = ComlexNum(12, 8)
    print(a, b)
    print(f"Результат  сложения: {a + b}")
    print(f"Результат  вычетания: {a - b}")
    print(f"Результат  умножения: {a * b}")
    print(f"Результат  деления: {a / b}")