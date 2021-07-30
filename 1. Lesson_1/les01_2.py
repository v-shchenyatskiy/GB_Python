# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды
# Выведите в формате чч:мм:сс. Используйте форматирование строк.

# 1 s * 60 = 1 m * 60 = 1h = 3600 s
# 1h * 24 = 1d = 86400 s

user_sec = int(input('Введите время в секундах: '))

# 1 - считаем часы
days = 0
hours = user_sec // 3600

if hours > 24:
    days = hours // 24
    hours = hours % 24

if (days // 10) < 1:
    days = f'0{days}'

if (hours // 10) < 1:
    hours = f'0{hours}'


# 2 - считаем минуты
minutes = (user_sec % 3600) // 60

if (minutes // 10) < 1:
    minutes = f'0{minutes}'


# 3 - считаем секунды
seconds = user_sec % 3600 % 60

if (seconds // 10) < 1:
    seconds = f'0{seconds}'


# 4 - Выводим результат
print(
    f'Вы ввели -> {user_sec}.\n'
    f'Это -> {days} {hours}:{minutes}:{seconds} (в формате DD hh:mm:ss)'
)
