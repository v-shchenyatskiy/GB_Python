# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.

# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв.м. дороги асфальтом, толщиной в 1 см * число см толщины полотна
# Проверить работу метода.

# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, length: int, width: int, depth=5, weight=25):
        self._length_m = length
        self._width_m = width
        self._depth_cm = depth
        self._weight_1cm_kg = weight

    def total_weight_kg(self):
        l, w, d, wt = self.__dict__.values()
        return l * w * d * wt

    def total_weight_tn(self):
        return self.total_weight_kg() / 1000


r = Road(5000, 20)
# print(r.total_weight_kg())
print(r.total_weight_tn())
