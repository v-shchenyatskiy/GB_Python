# Создать программно файл в текстовом формате.
# Записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

while True:
    user_str = input('Введите что-нибудь: ')
    if not user_str:
        break
    with open('les05_1.txt', 'a', encoding='utf-8') as my_file:
        print(user_str, file=my_file)
