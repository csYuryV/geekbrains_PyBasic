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


def outUserPersonalData(aName, aSurname, aYearOfBirth, aCityOfResidence, aEmail, aPhone):
    return  f'{aName} {aSurname}, дата рождения: {aYearOfBirth.strftime("%Y.%m.%d")}, город проживания: {aCityOfResidence.title()}, email: {aEmail}, тел.: {aPhone}.'

print(outUserPersonalData(aName='Сергей', aSurname='Прокопьев', aYearOfBirth=datetime.date(1975, 2, 19),
                          aCityOfResidence='Звездный Городок', aEmail='sergey.p@mks.ru', aPhone='+7 (495) 631-91-61'))

