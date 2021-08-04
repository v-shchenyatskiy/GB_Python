# * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# 1 Формируем шаблон структуры: (unique values)
_set = set()
while True:
    answer = int(input('Добавить параметр = 1, закончить = 2: '))
    if answer == 1:
        _set.add(input('Введите параметр товара: '))
    elif answer == 2:
        break

template = list(_set)
template.sort()
# template = ['название', 'цена', 'количество', 'ед.изм.']

print(f'Шаблон товара = {template}', '\n')

# 2 Создаем список товаров:  (any values)
products = []
while True:
    answer = int(input('Добавить продукт = 1, закончить = 2: '))
    if answer == 1:
        new_dict = {}
        for param in template:
            value = input(f'{param} товара: ')
            new_dict.update({param: value})

        idx = len(products)
        products.append((idx, new_dict))
    elif answer == 2:
        break

# products = [
#     (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'ед.изм.': 'шт.'}),
#     (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'ед.изм.': 'шт.'}),
#     (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'ед.изм.': 'шт.'})
# ]

print(f'Список товаров = {products}', '\n')

# 3 Готовим аналитику по Списку товаров: (unique values)
analysis_dict = {}

for param in template:
    values = set()
    for product in products:
        value = product[1][param]
        values.add(value)
    analysis_dict.update({param: list(values)})

print('Аналитика по товарам:')
print(f'Уникальные значения = {analysis_dict}', '\n')
