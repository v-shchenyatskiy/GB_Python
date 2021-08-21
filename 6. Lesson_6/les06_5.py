# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”

# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Marker (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.

# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title=''):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    # def __init__(self):
    #     super().__init__(title='ручка')

    def draw(self):
        print('Пишем ручкой')


class Pencil(Stationery):
    # def __init__(self):
    #     super().__init__(title='карандаш')

    def draw(self):
        print('Рисуем карандашом')


class Marker(Stationery):
    # def __init__(self):
    #     super().__init__(title='маркер')

    def draw(self):
        print('Хулиганим маркером')


pen = Pen()
pencil = Pencil()
marker = Marker()

pen.draw()
pencil.draw()
marker.draw()

# title не обязательный параметр, поэтому можно оставить только методы и все будет работать
