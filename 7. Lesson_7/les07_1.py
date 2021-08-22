# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.

# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно:
#  - первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix: list):
        self.line_len = max(map(len, matrix))
        self.matrix = [*(self.__align_list(el, self.line_len, 0) for el in matrix)]

    def __str__(self):
        max_n_len = max(map(lambda n: len(str(n)), sum(self.matrix, [])))

        for line in self.matrix:
            print(*['{:^{width}}'.format(n, width=max_n_len) for n in line])
        return ''

    def __add__(self, other):
        m_1 = self.matrix.copy()
        m_2 = other.matrix.copy()

        max_len = max(len(m_1), len(m_2))

        m_1 = self.__align_list(m_1, max_len)
        m_2 = self.__align_list(m_2, max_len)

        lines = zip(m_1, m_2)

        new_m = []
        for line in lines:
            max_len = max(len(line[0]), len(line[1]))
            l_1 = self.__align_list(line[0], max_len, 0)
            l_2 = self.__align_list(line[1], max_len, 0)
            new_m.append([*map(sum, zip(l_1, l_2))])

        return Matrix(new_m)

    def __align_list(self, l: list, length: int, el=1):
        el = [] if el else 0
        if len(l) < length:
            [l.append(el) for _ in range(length - len(l))]
        return l


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
# matrix_1 = Matrix([[1, 2], [3, 4], [5]])
# matrix_1 = Matrix([[1, 2], [3, 4], [5, 6, 7]])
# matrix_1 = Matrix([[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3]])
# matrix_1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])
# matrix_2 = Matrix([[1], [22], [333], [444]])
matrix_2 = Matrix([[1], [22], [333], [444], [55555], [666666]])

# print(matrix_1)
# print(matrix_2)
print(matrix_1 + matrix_2)
