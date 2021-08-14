# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и количество лекционных, практических и лабораторных занятий по этому предмету.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.

# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —

# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

from functools import reduce

with open('les05_6.txt', 'r', encoding='utf-8') as my_file:
    _lines = [line.split(':') for line in my_file.readlines()]

keys = [k for k, s in _lines]
strings = [s for k, s in _lines]

values = []
for s in strings:
    new_s = [char if char.isdigit() else ' ' for char in s]
    _nums = ''.join(new_s).split()
    values.append(reduce(lambda a, b: a + b, map(int, _nums)))

subj_dict = dict(zip(keys, values))
print(subj_dict)
