"""
Python Basic Lesson 03, Exercise 03

Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.

20191018 Sikorskiy Yuriy
cs.yury.v@pn.me

"""


def my_func(aVal1, aVal2, aVal3):
    """ принимает три позиционных аргумента,
    и возвращает сумму наибольших двух аргументов

    """
    return (sum(sorted([aVal1, aVal2, aVal3])[1:]))


print(my_func(4, 3, 2))
