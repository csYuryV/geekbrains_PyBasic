"""
Python Basic Lesson 04, Exercise 04

Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести
в порядке их следования в исходном списке. Для выполнения задания обязательно
использовать генератор.

20191018 Sikorskiy Yuriy
cs.yury.v@pn.me

"""
import random

sl = [random.randrange(50) for i in range(25)]
print(f'sl: {sl}.')
print(f'rs: {[el for el in sl if sl.count(el) == 1 ]}.')









