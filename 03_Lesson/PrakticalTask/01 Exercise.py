'''
Python Basic Lesson 03, Exercise 01

Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.


20191015 Sikorskiy Yuriy
cs.yury.v@pn.me

'''


def fDivision(aDividend, aDivider):
    """
    fDivision реализует деление float(aDividend) на float(aDivider).

    :param aDividend:
    :param aDivider:
    :return:
    """
    try:
        isDivisionByZero = True
        quotientFromDivision = aDividend / aDivider
        return quotientFromDivision, not isDivisionByZero
    except ZeroDivisionError:
        return None, isDivisionByZero


def isfloat(aValue):
    """fDivision проверяет возможность приведения переменной aValue к типу float
    :param value:
    :return:
    """
    try:
        float(aValue)
        return True
    except ValueError:
        return False


def inputNum(aInvite='Введите число'):
    """
    :param aInvite:
    :return:
    """
    while True:
        sFloat = input(aInvite)
        if sInt == '':
            return None
        if isfloat(sFloat):
            return float(sFloat)
        else:
            print(f"{sFloat} не относится к численному типу.")

print(
    'Чтобы получить частное от деления, введите значения делимого и делителя.\nДля завершения работы введите пустую строку.')
while True:
    dividend = inputNum('Введите делимое: ')
    if dividend is None:
        print('Программа завершена.')
        break
    divider = inputNum('Введите делитель: ')
    if divider is None:
        print('Программа завершена.')
        break
    quotientFromDivision, isDivisionByZero = fDivision(dividend, divider)
    if isDivisionByZero:
        print('В обычной арифметике (с вещественными числами) деление на ноль не имеет смысла.')
    else:
        print(f"{dividend} / {divider} = {quotientFromDivision}\n")
