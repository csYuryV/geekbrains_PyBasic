'''
Python Basic Lesson 06, Exercise 02

Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, т
олщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т


20191027 Sikorskiy Yuriy
cs.yury.v@pm.me

'''


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def getAsphaltMass(self, thickness=0.05, density=2500):
        return self._length * self._width * thickness * density


myRoad = Road(5000, 20)
print(myRoad.getAsphaltMass())
