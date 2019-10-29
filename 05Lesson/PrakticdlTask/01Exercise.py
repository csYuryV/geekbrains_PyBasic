"""
Python Basic Lesson 05, Exercise 01

Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

20191023 Sikorskiy Yuriy
cs.yury.v@pm.me

"""
import datetime

b = datetime.datetime.now()
fObj = open(b.strftime("%Y%m%d-%H%M%S") + '.txt', 'w')

while True:
    s = input('<-- ')
    if s == '':
        break
    fObj.write(s + '\n')
fObj.close()
