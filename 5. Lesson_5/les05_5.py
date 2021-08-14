# Создать (программно) текстовый файл.
# Записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from functools import reduce

end = 10
with open('les05_5.txt', 'w+', encoding='utf-8') as my_file:
    print(' '.join(map(str, range(1, end + 1))), end=' ', file=my_file)
    my_file.seek(0)
    print(reduce(lambda a, b: a + b, map(int, *[line.split() for line in my_file.readlines()])))
