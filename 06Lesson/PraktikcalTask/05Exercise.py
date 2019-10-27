'''
Python Basic Lesson 06, Exercise 05

Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.

20191027
 Sikorskiy Yuriy
cs.yury.v@pm.me

'''

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self):
        super().__init__('Шариковая ручка')

    def draw(self):
        print('Запуск отрисовки ручки')

class Pencil(Stationery):
    def __init__(self):
        super().__init__('Деревянный карандаш')

    def draw(self):
        print('Запуск отрисовки карандаша')

class Handle(Stationery):
    def __init__(self):
        super().__init__('Маркер')

    def draw(self):
        print('Запуск отрисовки маркера')


pen = Pen()
pencil = Pencil()
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()


