"""
Python Basic Lesson 04, Exercise 06a

Реализовать бесконечный итератор, генерирующий целые числа, начиная с указанного

20191018 Sikorskiy Yuriy
cs.yury.v@pm.me

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
