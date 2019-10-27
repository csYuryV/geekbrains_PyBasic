"""
Python Basic Lesson 05, Exercise 05

Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран.

20191023 Sikorskiy Yuriy
cs.yury.v@pm.me

"""

import random

filename = '05_listNums.txt'
while True:
    try:
        with open(filename, 'w', encoding='UTF-8') as fOut:
            fOut.write(' '.join([str(random.randrange(50)) for i in range(25)]))
        break
    except FileNotFoundError:
        open(filename, 'r', encoding='UTF-8').close()

with open(filename, encoding='UTF-8') as fIn:
    print(f'Сумма чисел из файла \'{fIn.name}\' равна: {sum(list(map(int, fIn.readline().split())))}')
