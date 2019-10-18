"""
Python Basic Lesson 03, Exercise 04

Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать
в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной
функции возведения числа в степень.

20191018 Sikorskiy Yuriy
cs.yury.v@pn.me

"""

def my_func(x, y):
    """ Возводит x в степень y, при условии что x - действительное положительное число,
    а y - отрицательное целое"""

    multiplication = x
    for i in range(-y-1):
        multiplication *= x

    return 1/multiplication


while True:
    try:
        x = float(input('Введите дествительное положительное число \'x\': '))
    except ValueError:
        print('Неккоректный ввод.')
        continue
    if not x > 0:
        print('Значение \'х\'должно быть положительным.')
    else:
        break
while True:
    try:
        y = int(input('Введите целое отричательное число \'y\': '))
    except ValueError:
        print('Неккоректный ввод.')
        continue
    if y >= 0:
        print('Значение \'y\' должно быть отрицательным.')
    else:
        break

print(f'my_func({x}, {y}) = {my_func(x, y)}, для проверки pow({x}, {y}) = {pow(x, y)}')
