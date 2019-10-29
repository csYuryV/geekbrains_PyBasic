'''
Python Basic Lesson 07, Exercise 02

Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.

20191029 Sikorskiy Yuriy
cs.yury.v@pm.me

'''

from abc import ABC as Abc, abstractmethod


class Clothes(Abc):  # Одежда
    @abstractmethod
    def calc_fabric_consumption(self):
        pass


class Coat(Clothes):  # Пальто
    def __init__(self, size):
        self._size = size

    def calc_fabric_consumption(self):
        return self._size / 6.5 + 0.5

    @property
    def size(self):
        return self._size


class Costume(Clothes):  # Костюм
    def __init__(self, height):
        self._height = height * 0.01

    def calc_fabric_consumption(self):
        return self._height * 2 + 0.3  # 2*H + 0.3

    @property
    def height(self):
        return self._height


def calc_total_fabric_area(amnf_clothes):
    total_fabric_area = 0.0
    for i in amnf_clothes:
        total_fabric_area += i[0].calc_fabric_consumption() * i[1]
    return total_fabric_area


mnf_clothes = []
mnf_clothes.append([Coat(40), 2])
mnf_clothes.append([Coat(42), 2])
mnf_clothes.append([Coat(44), 3])
mnf_clothes.append([Coat(46), 5])
mnf_clothes.append([Coat(48), 8])
mnf_clothes.append([Coat(50), 8])
mnf_clothes.append([Coat(52), 10])
mnf_clothes.append([Coat(54), 10])
mnf_clothes.append([Coat(56), 8])
mnf_clothes.append([Coat(58), 7])
mnf_clothes.append([Coat(60), 4])
mnf_clothes.append([Coat(62), 2])
mnf_clothes.append([Coat(64), 1])
mnf_clothes.append([Costume(154), 1])
mnf_clothes.append([Costume(160), 4])
mnf_clothes.append([Costume(166), 5])
mnf_clothes.append([Costume(172), 11])
mnf_clothes.append([Costume(178), 15])
mnf_clothes.append([Costume(184), 15])
mnf_clothes.append([Costume(190), 6])
mnf_clothes.append([Costume(196), 2])
mnf_clothes.append([Costume(202), 1])

print(f'{calc_total_fabric_area(mnf_clothes):0.2f}')
