# Создать текстовый файл (не программно)
# Сохранить в нем несколько строк
# Выполнить подсчет:
#  - количества строк
#  - количества слов в каждой строке.

with open('les05_2.txt', 'r', encoding='utf-8') as my_file:
    lines = my_file.readlines()
    print(f'Q строк в файле = {len(lines)}')
    [print(f'Q слов в строке_{idx} = {len(line.split())}') for idx, line in enumerate(lines, 1)]
