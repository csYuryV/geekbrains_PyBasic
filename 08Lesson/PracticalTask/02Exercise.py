'''
Python Basic Lesson 08, Exercise 02

20191102 Sikorskiy Yuriy
cs.yury.v@pm.me

Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.

'''


class My_division_by_zero(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    divisible, divisor = map(int, input(
        "Введите, через запятую, два целых положительных числа (делитель и делимое): ").split(','))
    if divisor == 0:
        raise My_division_by_zero('Попытка деления на ноль.')


except ValueError:
    print('Некоректный ввод')
except My_division_by_zero as e:
    print(e)
else:
    print(f'divisible/divisor = {divisible / divisor:0.2f}')
