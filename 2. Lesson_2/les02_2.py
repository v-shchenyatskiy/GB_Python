# Для списка реализовать обмен значений соседних элементов
# Т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

user_list = []

while True:
    inp_end = ' еще' if user_list else ''
    user_list.append(input(f'Введите что-нибудь{inp_end}: '))

    user_answer = input('Чтобы закончить - N, или нажмите Enter, чтобы продолжить: ')
    if user_answer.lower() == 'n':
        break

# Отладочные значения: (код выше можно закомментировать)
# user_list = [1, 2, 3, 4]
# user_list = [1, 2, 3, 4, 5]

print(f'Вы ввели = {user_list}')

i = 0
while i < len(user_list):
    r_list = user_list[i:i + 2]
    r_list.reverse()
    user_list[i:i + 2] = r_list
    i += 2

print(f'Вот что получилось = {user_list}')
