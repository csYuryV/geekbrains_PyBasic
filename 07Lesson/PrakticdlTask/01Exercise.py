'''
Python Basic Lesson 07, Exercise 01

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод __init__()), который должен принимать данные (список списков) для
формирования матрицы.

Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы. Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

20191029 Sikorskiy Yuriy
cs.yury.v@pm.me

'''
import numpy as np

class Matrix:
    def __init__(self, *args):
        self.value = np.array(args, int)

    def __str__(self):
        return str(self.value)

    def __call__(self):
        return self.value

    def __add__(self, other):
        try:
            temp = self.value + other()
        except Exception as e:
            print(e.__class__)
            return None
        return temp


# # mat1 и mat2  исходные матрицы одинакового размера
# res = [] # результирующая матрица
#
# i = 0
# while i < len(mat1):
#     res.append([])
#     j = 0
#     while j < len(mat1[i]):
#         res[i].append(mat1[i][j] + mat2[i][j])
#         j += 1
#     i += 1



my_matrix = Matrix([31, 22], [37, 43,], [51, 86])
my_matrix1 = Matrix([32, 2], [17, 34,])
my_matrix2 = Matrix([32, 2], [17, 34,], [43, 14])

print(my_matrix, '\n')
print(my_matrix1, '\n')

print(my_matrix + my_matrix1, '\n')
print(my_matrix + my_matrix2, '\n')