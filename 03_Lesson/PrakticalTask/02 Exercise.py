'''
Python Basic Lesson 03, Exercise 02

Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.


20191016 Sikorskiy Yuriy
cs.yury.v@pn.me

'''
import datetime


def outUserPersonalData(aName=None, aSurname=None, aYearOfBirth=None, aCityOfResidence=None, aEmail=None, aPhone=None):
    """
    outUserPersonalData формирует строку с персональных данных, переданных в аргументах функции
    :param aName:
    :param aSurname:
    :param aYearOfBirth:
    :param aCityOfResidence:
    :param aEmail:
    :param aPhone:
    :return:
    """
    sRes = None
    if aName is None and aSurname is None:
        sRes = 'Аноним.'
    else:
        if aName is not None:
            sRes = f'Имя: {aName.title()}.'

        if aSurname is not None:
            if sRes is not None:
                sRes = sRes[:-1] + ', фамилия: '
            else:
                sRes = 'Фамилия: '
            sRes += f'{aSurname.title()}.'
    if aYearOfBirth is not None:
        sRes = sRes[:-1] + f', дата рождения: {aYearOfBirth.strftime("%Y.%m.%d")}.'
    if aCityOfResidence is not None:
        sRes = sRes[:-1] + f', город проживания: {aCityOfResidence.title()}.'
    if aEmail is not None:
        sRes = sRes[:-1] + f', email: {aEmail}.'
    if aPhone is not None:
        sRes = sRes[:-1] + f', тел.: {aPhone}.'
    return sRes


print(outUserPersonalData(aName='Сергей', aSurname='Прокопьев', aYearOfBirth=datetime.date(1975, 2, 19), aCityOfResidence='Звездный Городок', aEmail='sergey.p@mks.ru', aPhone='+7 (495) 631-91-61'))
print(outUserPersonalData(aSurname='Прокопьев', aYearOfBirth=datetime.date(1975, 2, 19), aCityOfResidence='Звездный городок', aEmail='sergey.p@mks.ru', aPhone='+7 (495) 631-91-61'))
print(outUserPersonalData(aYearOfBirth=datetime.date(1975, 2, 19), aCityOfResidence='Звездный Городок', aEmail='sergey.p@mks.ru', aPhone='+7 (495) 631-91-61'))
print(outUserPersonalData(aYearOfBirth=datetime.date(1975, 2, 19), aCityOfResidence='Звездный Городок', aEmail='sergey.p@mks.ru'))
print(outUserPersonalData(aCityOfResidence='москва'))