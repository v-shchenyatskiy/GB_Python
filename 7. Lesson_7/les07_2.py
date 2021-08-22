# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.

# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры:
#  - размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.

# Для определения расхода ткани по каждому типу одежды использовать формулы:
#  - для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.

# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
#  - реализовать абстрактные классы для основных классов проекта,
#  - проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def outgo(self):
        """Суммарный расход ткани"""
        pass


class Coat(Clothes):
    def __init__(self, size_eu: float, qty=1):
        self.v = size_eu
        self.qty = qty

    def __str__(self):
        return f'Кол-во изделий {self.qty}, суммарный расход ткани {self.outgo} м'

    @property
    def outgo(self):
        return round((self.v / 6.5 + 0.5) * self.qty, 2)


class Suit(Clothes):
    def __init__(self, height_cm: float, qty=1):
        self.h = height_cm
        self.qty = qty

    def __str__(self):
        return f'Кол-во изделий {self.qty}, суммарный расход ткани {self.outgo} м'

    @property
    def outgo(self):
        return round((2 * self.h / 100 + 0.3) * self.qty, 2)


c = Coat(56, 5)
s = Suit(182, 7)

print(c)
print(s)
