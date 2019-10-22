"""
Python Basic Lesson 05, Exercise 05


Реализовать формирование списка, используя функцию range() и возможности генератора. В
список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().

20191019 Sikorskiy Yuriy
cs.yury.v@pm.me

"""
from functools import reduce

sl = [el for el in range(100, 1001, 2)]
print(sl)


def reducer_func(el_prev, el):
    # el_prev — предшествующий элемент
    # el — текущий элемент
    return el_prev * el

print(reduce(reducer_func, sl))

# P.S. На просторах интернета нашел следубщее мнение:
# Python 3 Настоятельно рекомендуется использовать обычный проход по элементам при помощи for
# для повышения читаемости кода. https://pythonz.net/references/named/reduce/

