# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

user_num = int(input('Введите число: '))

num_2 = int(f'{user_num}{user_num}')
num_3 = int(f'{user_num}{user_num}{user_num}')

print(f'Вы ввели: {user_num}')
print(f'Итого: {user_num} + {num_2} + {num_3} = {user_num + num_2 + num_3}')
