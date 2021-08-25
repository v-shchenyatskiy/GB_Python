# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDivErr(Exception):
    def __str__(self):
        return 'Ошибка! Деление на ноль!'


while True:
    try:
        a = int(input('Введите число_1: '))
        b = int(input('Введите число_2: '))
        if not b:
            raise ZeroDivErr
    except ValueError:
        print('Ошибка! Следует ввести число!')
    except ZeroDivErr as err:
        print(err)
    else:
        print(a / b)
        break
