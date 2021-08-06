# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

# 1 Вариант (в одну строчку)
def my_func_1(x1: int, x2: int, x3: int):
    return max(sum([x1, x2]), sum([x2, x3]), sum([x3, x1]))


# 2 Вариант
def my_func_2(x1: int, x2: int, x3: int):
    _list = [x1, x2, x3]
    _list.sort()
    return sum(_list[-2:])


# 3 Вариант (более универсальный)
def my_func_3(x1: int, x2: int, *args: int):
    _list = sum([[x1, x2], list(args)], [])
    _list.sort()
    return sum(_list[-2:])


print(
    # my_func_1(
    # my_func_2(
    my_func_3(
        int(input('Введите число: ')),
        int(input('Введите число: ')),
        int(input('Введите число: ')),
        # int(input('Введите число: ')),
        # int(input('Введите число: ')),
        # int(input('Введите число: ')),
        # int(input('Введите число: ')),
        # int(input('Введите число: ')),
        # int(input('Введите число: ')),
    )
)
