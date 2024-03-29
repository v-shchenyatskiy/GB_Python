# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [
    # целое число (int)
    12345,

    # дробное число (float)
    12345.99,

    # строка (str)
    '12345',
    'one two three four five',

    # список (list)
    [12345, '12345'],
    list('12345'),

    # кортеж (tuple)
    (12345, '12345'),
    tuple('12345'),

    # множество (set и frozenset)
    {1, 2, 3},
    frozenset({1, 2, 3}),
    set('123'),
    frozenset('123'),

    # словарь (dict)
    {'one': 1, 'two': 2},
    dict(one=1, two=2),

    # булеан (bool)
    True,
    False,

    # байты (bytes и bytearray)
    b'text',
    bytes(b'text'),
    bytearray(b'text'),

    # NoneType
    None,
]

for el in my_list:
    print(f'Элемент = {el}, тип элемента = {type(el)}')
