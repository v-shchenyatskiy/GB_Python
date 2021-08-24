# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_num = int(input('Введите число: '))

the_biggest_num = 0
check_num = user_num

while check_num > 0:
    last_num = check_num % 10
    check_num = check_num // 10

    if last_num > the_biggest_num:
        the_biggest_num = last_num

print(f'Вы ввели: {user_num}')
print(f'Самая большая цифра в числе: {the_biggest_num}')
