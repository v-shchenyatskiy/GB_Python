# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class MyComplex:
    def __init__(self, a: int, b: int):
        self.__a = a
        self.__b = b

    def __str__(self):
        return f'({self.__a}+{self.__b}j)'

    def __add__(self, other):
        a1, a2, b1, b2 = self.__a, other.__a, self.__b, other.__b
        return MyComplex(a=(a1 + a2), b=(b1 + b2))

    def __mul__(self, other):
        a1, a2, b1, b2 = self.__a, other.__a, self.__b, other.__b
        return MyComplex(a=(a1 * a2 - b1 * b2), b=(a1 * b2 + a2 * b1))


x = MyComplex(1, 2)
y = MyComplex(3, 4)

print(x, y)  # (1+2j) (3+4j)
print(x + y)  # (4+6j)
print(x * y)  # (-5+10j)
