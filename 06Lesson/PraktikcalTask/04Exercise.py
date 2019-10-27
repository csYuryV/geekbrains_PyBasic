'''
Python Basic Lesson 06, Exercise 04

Опишите несколько классов: TownCar, SportCar, WorkCar, PoliceCar. У каждого класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также несколько методов: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

20191027 Sikorskiy Yuriy
cs.yury.v@pm.me

'''

LEFT = 1
RIGHT = 2
STRONG = 3
BACKING_UP = 4


class Car:

    def __init__(self, name, color, is_police):
        self.name = name
        self.color = color
        self.is_police = is_police
        self._speed = 0
        self._direction_of_travel = STRONG


    def go(self):
        self._speed = 55
        print(f'{self.name} начал движение')
        return self._speed

    def stop(self):
        if self._speed != 0:
            self._speed = 0
            print(f'{self.name} остановился')
        else:
            print(f'{self.name} стоит')
        return self._speed

    def turn(self, which_way):
        if self._speed != 0:
            if which_way == LEFT:
                self._direction_of_travel = LEFT
                print(f'{self.name} поворачивает налево')
            elif which_way == RIGHT:
                self._direction_of_travel = RIGHT
                print(f'{self.name} поворачивает направо')
            elif which_way == STRONG:
                self._direction_of_travel = STRONG
                print(f'{self.name} двигается прямо')
            elif which_way == BACKING_UP:
                self._direction_of_travel = BACKING_UP
                print(f'{self.name} сдает задним ходом')
        else:
            print(f'{self.name} стоит')

    def get_direction_of_travel(self):
        return self._direction_of_travel


class TownCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, False)


class SportCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, False)


class WorkCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, False)


class PoliceCar(Car):
    def __init__(self,  name, color):
        super().__init__(name, color, True)
        self._special_signal = False


    def turn_on_the_special_signal(self):
        self.special_signal = True
        print(f'{self.name} включил спецсигналы')
        return self._special_signal

    def turn_off_the_special_signal(self):
        self.special_signal = False
        print(f'{self.name} выключил спецсигналы')
        return self._special_signal



townCar = TownCar('Renault Twingo', 'Белый')
sportCar = SportCar('911 Carrera', 'Красный')
workCar = WorkCar('Ford F-100', 'Красный')
policeCar = PoliceCar('RAM 1500 SPECIAL SERVICE', 'Черно-белый')


policeCar.go()
policeCar.turn(STRONG)
policeCar.turn_on_the_special_signal()
policeCar.turn(LEFT)
policeCar.turn(STRONG)
policeCar.stop()
policeCar.turn_off_the_special_signal()






