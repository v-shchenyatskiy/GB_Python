# Поработайте с переменными:
# - 1 создайте несколько и выведите на экран
# - 2 запросите у пользователя несколько чисел и строк, сохраните их в переменные, выведите на экран.

# 1
my_num = 12345
my_str = '12345'

print(f'Числовая переменная my_num = {my_num}')
print(f'Строковая переменная my_str = {my_str}')

# 2
user_num_1 = int(input('Введите любое число: '))
user_num_2 = int(input('Еще раз введите любое число: '))
user_num_3 = int(input('Ну и еще разок введите любое число: '))

print(
    f'Итак вы ввели: '
    f'первое число = {user_num_1}, '
    f'второе число = {user_num_2}, '
    f'третье число = {user_num_3}'
)
print(
    f'Типы: '
    f'user_num_1 = {type(user_num_1)}, '
    f'user_num_2 = {type(user_num_2)}, '
    f'user_num_3 = {type(user_num_3)}'
)

user_str_1 = input('Введите любую строку: ')
user_str_2 = input('Еще раз введите любую строку: ')
user_str_3 = input('Ну и еще разок введите любую строку: ')

print(
    f'Итак вы ввели: '
    f'первая строка = {user_str_1}, '
    f'вторая строка = {user_str_2}, '
    f'третая строка = {user_str_3}'
)
print(
    f'Типы: '
    f'user_str_1 = {type(user_str_1)}, '
    f'user_str_2 = {type(user_str_2)}, '
    f'user_str_3 = {type(user_str_3)}'
)
