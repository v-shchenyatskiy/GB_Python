# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов.
# Вывести фамилии сотрудников с окладом менее 20 тыс.
# Выполнить подсчет средней величины дохода сотрудников.

with open('les05_3.txt', 'r', encoding='utf-8') as my_file:
    print(*[(line.split())[0] for line in my_file.readlines() if float((line.split())[1]) < 20_000.0])
