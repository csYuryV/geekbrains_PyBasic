"""
Python Basic Lesson 04, Exercise 03

Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.


20191019 Sikorskiy Yuriy
cs.yury.v@pn.me

"""
print([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0])
