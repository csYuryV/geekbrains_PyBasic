'''
Python Basic Lesson 03, Exercise 01

Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.

20191015 Sikorskiy Yuriy
cs.yury.v@pn.me

'''


def fDivision(aDividend, aDivider):
    try:
        return float(aDividend) / float(aDivider)
    except ValueError:
        return "Value error"
    except ZeroDivisionError:
        return "Division by zero"


print(fDivision(input('Enter dividend: '), input('Enter divider: ')))
