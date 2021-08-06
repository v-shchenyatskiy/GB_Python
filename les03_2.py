# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
#  - имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def print_user_profile(name: str, phone: int, **kwargs):
    profile = {'name': name, 'phone': phone}
    profile.update(kwargs)
    print('Создан профиль пользователя: ')
    print(profile, end='')


print('Введите ваши данные:')
print_user_profile(
    name=input('Имя: '),
    surname=input('Фамилия: '),
    date_of_birth=input('День рождения: '),
    city=input('Город проживания: '),
    email=input('Эл.почта: '),
    phone=int(input('Контактный телефон: ')),
)
