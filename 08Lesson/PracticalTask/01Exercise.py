'''
Python Basic Lesson 08, Exercise 01

20191102 Sikorskiy Yuriy
cs.yury.v@pm.me

Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры
на реальных данных.


'''

import re


class This_date:
    def __init__(self, sdate=''):
        self._ldate = []
        if sdate != '':
            self._ldate = self.in_date(sdate)

    @classmethod
    def in_date(self, sdate):
        res = re.search(r'(0[1-9]|1[0-9]|2[0-9]|3[01])-(0[1-9]|1[012])-[0-9]{4}\b', sdate)
        if res is not None:
            res = res.group(0)
            res = res.split('-')
            res = list(map(int, res))
            res.reverse()
            if not This_date.has_date_validity(res[0], res[1], res[2]):
                return []
            return res
        return []

    @staticmethod
    def has_date_validity(year, month, day):
        if month in [4, 6, 9, 11] and day > 30:
            # Если месяц апрель, июнь, сентябрь, ноябрь и день больше 30
            return False
        if month == 2 and ((year % 4 != 0 and day > 28) or (year % 4 == 0 and day > 29)):
            # Если месяц февраль(2) и ((год невысокосный и день больше 28) или (год высокосный и день больше 29))
            return False
        return True

    def __call__(self):
        return self._ldate


sdate = 'В этот день: 27-12-1597 родился великий украинский гетман Зиновий Богдан Хмельницкий'

my_date = This_date(sdate)
print(sdate + ': ', my_date())

print('28-02-2035:', This_date.in_date('28-02-2035'))
print('30-04-2035:', This_date.in_date('30-04-2035'))
print('31-04-2035:', This_date.in_date('31-04-2035'))
print('29-02-2036:', This_date.in_date('29-02-2036'))
print('29-02-2035:', my_date.in_date('29-02-2035'))

