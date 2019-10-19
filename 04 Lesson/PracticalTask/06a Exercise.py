"""
Python Basic Lesson 03, Exercise 06

Реализовать бесконечный итератор, генерирующий целые числа, начиная с указанного

20191018 Sikorskiy Yuriy
cs.yury.v@pn.me

"""
import itertools

try:
    iBegin = int(input('Укажите число с которого начать итерацию: '))

except ValueError:
    print('Ошибка значения')
    exit(-1)

for i in itertools.count(start=iBegin, step=1):
    print(i)

# P.S. Предупреждение: реализован бесконечный цикл. На это можно долго смотреть
