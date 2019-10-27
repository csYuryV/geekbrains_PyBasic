'''
Python Basic Lesson 06, Exercise 03

Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"profit": profit, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_full_profit). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


20191027 Sikorskiy Yuriy
cs.yury.v@pm.me

'''


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):

    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_full_profit(self):
        return self._income['profit'] + self._income['bonus']


income = {"profit": 150000, "bonus": 75000}
person = Position('Эдвард', 'Сноуден', 'Охранник', income)

print(person.get_full_name())
print(person.get_full_profit())
