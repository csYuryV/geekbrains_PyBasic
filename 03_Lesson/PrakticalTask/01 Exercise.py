'''
Python Basic Lesson 03, Exercise 01

Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.


0191015 Sikorskiy Yuriy
cs.yury.v@pn.me

'''


def fDivision(aDividend, aDivider):
    try:
        isDivisionByZero = True
        quotientFromDivision = aDividend / aDivider
        return quotientFromDivision, not isDivisionByZero
    except ZeroDivisionError:
        return None, isDivisionByZero


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def inputNum(aInvite='Введите число'):
    while True:

        sInt = input(aInvite)
        if sInt == '':
            return None
        if isfloat(sInt):
            return float(sInt)
        else:
            print(f"{sInt} не относится к численному типу.")


while True:
    dividend = inputNum('Введите делимое: ')
    if dividend is None:
        print('Задача завершена.')
        break
    divider = inputNum('Введите делитель: ')
    if divider is None:
        print('Задача завершена.')
        break
    quotientFromDivision, isDivisionByZero = fDivision(dividend, divider)
    if isDivisionByZero:
        print('В обычной арифметике (с вещественными числами) деление на ноль не имеет смысла.')
    else:
        print(f"{dividend} / {divider} = {quotientFromDivision}\n")
