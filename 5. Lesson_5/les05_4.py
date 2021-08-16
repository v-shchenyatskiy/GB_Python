# Создать (не программно) текстовый файл со следующим содержимым:
# One - 1
# Two - 2
# Three - 3
# Four - 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

src = ['Один', 'Два', 'Три', 'Четыре']
with open('les05_4.txt', 'r', encoding='utf-8') as my_file:
    with open('les05_4_new.txt', 'w', encoding='utf-8') as new_file:
        _lines = [line.split() for line in my_file.readlines()]
        [print(' '.join([src[i], *line[1:]]), file=new_file) for i, line in enumerate(_lines)]
