# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

# user_str = input('Введите несколько слов: ')

user_str = 'one two three four five01234567890'

print(f'Вы ввели = {user_str}')

print('Вот что получилось: ')

words = user_str.split()

i = 1
for w in words:
    print(f'{i}) {w[:10]}')
    i += 1
