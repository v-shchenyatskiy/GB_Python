# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def divide_xy(x: int, y: int):
    """
    Возвращает  частное от деления.

    (number, number) -> number | ZeroDivisionError

    >>> divide_xy(10, 2) -> 5
    """
    return ZeroDivisionError if y == 0 else x / y


print(divide_xy(int(input('Введите число x: ')), int(input('Введите число y: '))))

# print(divide_xy(5, 7))  # -> 0.7142857142857143
# print(divide_xy(5, 0))  # -> <class 'ZeroDivisionError'>
# print(divide_xy('5', '0'))  # -> TypeError: unsupported operand type(s) for /: 'str' and 'str'
