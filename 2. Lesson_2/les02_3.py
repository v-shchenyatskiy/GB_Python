# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons_dict = {
    'Winter': [1, 2, 12],
    'Spring': [3, 4, 5],
    'Summer': [6, 7, 8],
    'Autumn': [9, 10, 11],
}
months_dict = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
}
months_list = list(months_dict.values())

# month = 0
#
# while True:
#     month = int(input('Введите число месяца: '))
#     if 0 < month < 13:
#         break
#     print('Вы ввели неверное число. Повторите ввод')

month = 8

print(f'Вы ввели = {month}')

print(f'В словаре это = {months_dict[month]}')
print(f'В списке это = {months_list[month - 1]}')

# Поиск по сезонам - Вариант 1
for season in seasons_dict.items():
    for month_num in season[1]:
        if month_num == month:
            print(f'В словаре сезонов это = {season[0]}')

# Поиск по сезонам - Вариант 2
for season in seasons_dict:
    for month_num in seasons_dict[season]:
        if month_num == month:
            print(f'В словаре сезонов это = {season}')

# Поиск по сезонам - Вариант 3
for s in seasons_dict:
    for m in seasons_dict[s]:
        if m == month:
            print(f'В словаре сезонов это = {s}')
