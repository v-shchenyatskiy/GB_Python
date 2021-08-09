# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

print(reduce(lambda n_1, n_2: n_1 * n_2, [i for i in range(100, 1001) if not (i % 2)]))
