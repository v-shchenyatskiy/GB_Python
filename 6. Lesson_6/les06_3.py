# Реализовать базовый класс Worker (работник)
# В котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
#  - оклад и премия
# Например, {"wage": wage, "bonus": bonus}.

# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы:
#  - получения полного имени сотрудника (get_full_name) и
#  - дохода с учетом премии (get_total_income).

# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = lambda: {'wage': self.wage, 'bonus': self.bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income().values())


p = Position('Иван', 'Иванов', 'юрист', 10_000, 5_000)
print(p.get_full_name())
print(p.get_total_income())
print(p.position)

print()

p.name = 'Петр'
p.surname = 'Петров'
p.position = 'бухгалтер'
p.wage = 7_000
p.bonus = 3_000
print(p.get_full_name())
print(p.get_total_income())
print(p.position)
