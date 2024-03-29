# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

# Примечание:
# Длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.

# Подсказка:
# Для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

class MyNums(Exception):
    def __init__(self):
        self.nums = []
        while True:
            try:
                user_str = input('Введите число или stop, чтобы закончить: ')
                if user_str == 'stop':
                    break

                _num = float(user_str)
            except ValueError as err:
                print('Ошибка! Следует ввести число!')
            else:
                self.nums.append(_num)

    def __str__(self):
        return f'{self.nums}'


my_nums = MyNums()
print(my_nums)
