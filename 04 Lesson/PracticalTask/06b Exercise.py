"""
Python Basic Lesson 04, Exercise 06b

Реализовать бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.

20191018 Sikorskiy Yuriy
cs.yury.v@pm.me

"""
import itertools
import random

for i in itertools.cycle([random.randrange(50) for i in range(25)]):
    print(i)

# P.S. Предупреждение: реализован бесконечный цикл. На это можно долго смотреть
