# Реализовать класс Matrix (матрица). Обеспечить перегрузку
# конструктора класса (метод __init__()), который должен принимать
# данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# Следующий шаг — реализовать перегрузку метода __str__() для
# вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации
# операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять
# поэлементно — первый элемент первой строки первой
# матрицы складываем с первым элементом первой строки
# второй матрицы и т.д.

from copy import deepcopy

class Matrix:
    def __init__(self, a):
        self.a = deepcopy(a)

    def __str__(self):
         return '\n'.join('\t'.join(map(str, row))
                          for row in self.a)

    def printMatrix(self):

        for row in self.a:
            for x in row:
                print("{:4d}".format(x), end="")
            print()

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.a)):
            for j in range(len(self.a[0])):
                summa = other.a[i][j] + self.a[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.a):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


m1 = Matrix([[1, 0, 0], [1, 1, 1], [0, 0, 0]])
m2 = Matrix([[2, 1, 1], [2, 2, 2], [1, 1, 1]])
m5 = Matrix([[5, 0, 3], [3, 2, 1], [1, 0, 0]])
m6 = Matrix([[1, 3, 1], [2, 0, 2], [1, 8, 1]])

print(f'Матрица m6:\n{m6}')
print(f'Сумма m1+m2:\n{m1+m2}')
print(f'Сумма m5+m6:\n{m5+m6}')
print(f'Сумма m1+m6:\n{m1+m6}')
print(f'Матрица m1:\n{m1}')

m7 = Matrix([[1,2,3,4], [1,0,1,2]])
m8 = Matrix([[1,0,0,1], [1,1,1,1]])
m9 = m7 + m8
m9.printMatrix()




