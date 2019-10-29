'''
Python Basic Lesson 06, Exercise 01

Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный,
желтый, зеленый. Время перехода между режимами должно составлять 7 и 2 секунды. Проверить работу примера,
создав экземпляр и вызвав описанный метод.


20191027 Sikorskiy Yuriy
cs.yury.v@pm.me

'''

from sty import fg
import time
import threading


class Light_signal:
    def __init__(self, name, style_on, style_off):
        self.set_style(name, style_on, style_off)
        self._switch = False

    def set_style(self, name, style_on, style_off):
        self._name = name
        self._set_style_on(style_on)
        self._set_style_off(style_off)

    def _set_style_on(self, style_on):
        self._style_on = style_on

    def _set_style_off(self, style_off):
        self._style_off = style_off

    def switch_on(self):
        self._switch = True

    def switch_off(self):
        self._switch = False

    def get_switch(self):
        return self._name + ' - on,  ' if self._switch else self._name + ' - off, '

    def getDraw(self):
        if self._switch:
            view = self._style_on + '(@)' + fg.rs
        else:
            view = self._style_off + '(@)' + fg.rs
        return view


class TrafficLight:
    def __init__(self):
        self.color = ''
        self._lights = []
        self._lights.append(Light_signal('Green', fg.green, fg.rs))
        self._lights.append(Light_signal('Yellow', fg.yellow, fg.rs))
        self._lights.append(Light_signal('Red', fg.red, fg.rs))

        self._switchup_order = []
        self._switchup_order.append([0, self._lights[0].switch_on])
        self._switchup_order.append([7, self._lights[0].switch_off])
        self._switchup_order.append([7, self._lights[1].switch_on])
        self._switchup_order.append([9, self._lights[1].switch_off])
        self._switchup_order.append([9, self._lights[2].switch_on])
        self._switchup_order.append([14, self._lights[1].switch_on])
        self._switchup_order.append([0, self._lights[1].switch_off])
        self._switchup_order.append([0, self._lights[2].switch_off])
        self._cycle_time = 16
        self._current_measure = 0
        self._draw()

    def running(self):
        for i in self._switchup_order:
            if self._current_measure == i[0]:
                i[1]()
                self.color = ''
                self._redraw = True
        if self._redraw:
            self._draw()
        self._current_measure = self._current_measure + 1 if self._current_measure < self._cycle_time else 0

    def get_color(self):
        self.color = ''
        for i in self._lights:
            self.color = self.color + i.get_switch()
        self.color = self.color[:-2]
        if self.color[-1] == ',':
            self.color = self.color[:-1]
        return self.color

    def _draw(self):
        view = ''
        for i in self._lights:
            view = view + i.getDraw() + '-'
        view = view + '     self.color = ' + self.get_color()
        print('\r' + view, end='', flush=True)
        self._redraw = False
        pass


print('Press <Enter> to exit.')
trafficLight = TrafficLight()


def loop():
    while True:
        trafficLight.running()
        time.sleep(1)


threading.Thread(target=loop, daemon=True).start()
input('')

5 + 5
