# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, dd_mm_yyyy: str):
        d, m, y = self.parse(dd_mm_yyyy)

        self.day = d
        self.month = m
        self.year = y

    @classmethod
    def parse(cls, date: str):
        try:
            d, m, y = map(int, date.split('-', 3))
        except ValueError:
            print('Неверный формат даты. Введено:', date)
            print('Введите дату в формате dd-mm-yyyy. Например, 01-01-1970')
            return None, None, None
        else:
            return cls.validate(d, m, y)

    @staticmethod
    def validate(d: int, m: int, y: int):
        try:
            months = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
            if not ((d in range(1, months[m])) and (m in range(1, 12)) and (y in range(1, 9999))):
                raise KeyError
        except KeyError:
            print('Нарушен диапазон даты. Введено:', d, m, y)
            return None, None, None
        else:
            return d, m, y


my_date = Date('23-08-2021')
# my_date = Date('23.08.2021')
# my_date = Date('32-08-2021')
# my_date = Date('23-13-2021')
# my_date = Date('23-08-20211')
# my_date = Date('as-08-2021')

print(my_date.day)
print(my_date.month)
print(my_date.year)
