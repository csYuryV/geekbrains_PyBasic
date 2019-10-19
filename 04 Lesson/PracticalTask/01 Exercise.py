"""
Python Basic Lesson 04, Exercise 01

Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами.

20191019 Sikorskiy Yuriy
cs.yury.v@pn.me

"""
payroll = lambda productionInHours, paymentRatePerHour, premium: (productionInHours * paymentRatePerHour) + premium

try:
    wage = payroll(float(input('Выработка в часах: ')), float(input('Ставка в час: ')), float(input('Премия: ')))

except ValueError:
    print('Ошибка значения')
    exit()
print(f'Расчет заработной платы сотрудника: {wage:.2f}')
