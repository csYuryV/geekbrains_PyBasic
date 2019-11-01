'''
Python Basic Lesson 07, Exercise 03

Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться
только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток,
соответственно. В методе деления должно осуществляться округление значения до целого числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек
    двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение
    количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное
    деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.

20191101 Sikorskiy Yuriy
cs.yury.v@pm.me

'''


class Cell:
    def __init__(self, name, number_of_yacheek):
        self.name = name
        self.number_of_yacheek = number_of_yacheek
        # Я знаю, что использование транслита при наименовании переменных - дурной тон.
        # Вместе с этим, какая задача - такое и решение. В контексте задания предложены названия
        # "клетка", "ячейка", которые на бедный английский переводятся одним словом "cell"
        # Поэтому, чтобы различать понятия констекта задачи, я буду прменять для "клетка" перевод "cell"
        # для "ячейка" транслит "yacheyka"

    def __str__(self):
        return f'Ячеик в клетке {self.name}: {self.number_of_yacheek}'

    def __add__(self, other):
        return Cell(f'{self.name} + {other.name}', self.number_of_yacheek + other.number_of_yacheek)

    def __sub__(self, other):
        yacheek_subtraction_result = self.number_of_yacheek - other.number_of_yacheek
        # Чтоб не сложилось впечатление, что я просто переписал вариант решения, который обсуждался на вебинаре
        # Предполагаю, что эту проверку предусмотрели не все студенты
        # Не исключаю, что я единственный, кто предусмотрел =)
        if yacheek_subtraction_result >= 0:
            return Cell(f'{self.name} - {other.name}', yacheek_subtraction_result)
        else:
            print(f'({self.name} - {other.name}) < 0')
            return None

    def __mul__(self, other):
        return Cell(f'{self.name} * {other.name}', self.number_of_yacheek * other.number_of_yacheek)

    def __truediv__(self, other):
        # Чтоб не сложилось впечатление, что я просто переписал вариант решения, который обсуждался на вебинаре
        # Предполагаю, что эту проверку предусмотрели не все студенты
        # Не исключаю, что я единственный, кто предусмотрел =)
        try:
            yacheek_division_result = round(self.number_of_yacheek / other.number_of_yacheek)
        except ZeroDivisionError:
            print(
                f'{self.name} / {other.name}, как выяснили британские ученые, не имеет смысла.\nКлетка {other.name} содержит 0 ячеек')
            return None
        return Cell(f'{self.name} / {other.name}', yacheek_division_result)

    def make_order(self, number_of_yacheek_in_row):
        number_rows = self.number_of_yacheek // number_of_yacheek_in_row
        yacheek_division_remainder = self.number_of_yacheek % number_of_yacheek_in_row

        view_of_the_filled_line = ''
        if number_rows != 0:
            view_of_the_filled_line = '*' * number_of_yacheek_in_row + '\n'

        view_of_a_partially_filled_line = ''
        if yacheek_division_remainder != 0:
            view_of_a_partially_filled_line = '*' * yacheek_division_remainder + '\n'

        return view_of_the_filled_line * number_rows + view_of_a_partially_filled_line

    def draw(self, number_of_yacheek_in_row):
        if self.number_of_yacheek == 0:
            print(f'{self.name}\nпустая клетка')
        else:
            print(f'{self.name}\n{self.make_order(number_of_yacheek_in_row)}'[:-1])


class Separator:
    def __init__(self, length):
        self.length = length

    def draw(self):
        print('+' + '-' * (self.length - 2) + '+')


LENGTH_SEPARATOR = 20
separator = Separator(LENGTH_SEPARATOR)

LENGTH_ROW = 6

cell_1 = Cell('cell_1', 27)
cell_2 = Cell('cell_2', 11)

cell_1.draw(LENGTH_ROW)
cell_2.draw(LENGTH_ROW)
res_cell = cell_1 + cell_2
res_cell.draw(LENGTH_ROW)
separator.draw()

res_cell = cell_1 - cell_2
if res_cell is not None:
    res_cell.draw(LENGTH_ROW)
separator.draw()

res_cell = cell_2 - cell_1
if res_cell is not None:
    res_cell.draw(LENGTH_ROW)
separator.draw()

res_cell = cell_1 * cell_2
res_cell.draw(LENGTH_ROW)
separator.draw()

res_cell = cell_1 / cell_2
if res_cell is not None:
    res_cell.draw(LENGTH_ROW)
separator.draw()

zero = Cell('zero', 0)
zero.draw(LENGTH_ROW)

res_cell = cell_1 / zero
if res_cell is not None:
    res_cell.draw(LENGTH_ROW)
separator.draw()
