'''
Python Basic Lesson 08, Exercise 04

20191102 Sikorskiy Yuriy
cs.yury.v@pm.me



'''
import datetime
from abc import ABC, abstractmethod
from view import Show_dict_cards, Show_dict_storage_points, Show_balans_storage_point


class Essence:
    def __init__(self, name):
        self._name = name
        self._id = None

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name


class Dict_entities(dict):
    def __init__(self, name):
        super().__init__()
        self._name = name
        self._id_counter = 0

    def add(self, essence):
        essence.set_id(self._id_counter)
        self[self._id_counter] = essence
        self._id_counter += 1
        return essence.get_id()

    def get_name(self):
        return self._name


class Dict_cards(Dict_entities):
    def __init__(self):
        super().__init__('Список карточек ТМЦ')


class Card_item(Essence):
    def __init__(self, name, description=''):
        super().__init__(name)
        # description - описание ТМЦ
        # price - цена за единицу
        self._description = description

    def get_description(self):
        return self._description


class Dict_storage_points(Dict_entities):
    def __init__(self):
        super().__init__('Список точек хранения и контрагентов.')


class Dict_move_item(Dict_entities):
    def __init__(self, name):
        super().__init__(name)


class Record_move_item(Essence):
    # Запись в амбарную книгу о перемещении ТМЦ
    def __init__(self, dttm, st_pnt, move_st_pnt, card, quantity):
        super().__init__('')
        # dttm - дата и время двиения ТМЦ
        # id_st_pnt -  id точки хранения
        # id_move - id кореспондирующей точки хранения. Если приход то откуда, если расход то куда
        # произоло перемещение ТМЦ
        # id_card - id карточки ТМЦ
        # quantity - количество перемещаемых едениц ТМЦ если положительное то приход, если отрицательное то расход
        self._dttm = dttm
        self._st_pnt = st_pnt
        self._move_st_pnt = move_st_pnt
        self._card = card
        self._quantity = quantity

    def get_dttm(self):
        return self._dttm

    def get_card(self):
        return self._card

    def get_quantity(self):
        return self._quantity


class Movable_item:
    def __init__(self, st_pnt, card, quantity):
        self._st_pnt = st_pnt
        self._card = card
        self._quantity = quantity

    def get_st_pnt(self):
        return self._st_pnt

    def get_card(self):
        return self._card

    def get_quantity(self):
        return self._quantity


class Storage_point(Essence):
    def __init__(self, name, description, provider, dict_move_item, dict_cards):
        super().__init__(name)
        self._description = description
        self._provider = provider  # True - организация поставщик, False - точка хранения
        self._dict_move_item = dict_move_item
        self._dict_cards = dict_cards
        self._list_id_move_items = []

    def get_description(self):
        return self._description

    def get_provider(self):
        return self._provider

    def income(self, movable_item):
        record_move_item = Record_move_item(datetime.datetime.now(), self, movable_item.get_st_pnt(),
                                            movable_item.get_card(), movable_item.get_quantity())

        self._list_id_move_items.append(self._dict_move_item.add(record_move_item))
        # self._dict_move_items.add
        #
        #
        #
        pass

    def flow(self, new_st_pnt, card, quantity):
        if self.calc_balance(card) >= quantity:
            record_move_item = Record_move_item(datetime.datetime.now(), self, new_st_pnt, card, -quantity)

            #      добавляю запись о расходе
            self._list_id_move_items.append(self._dict_move_item.add(record_move_item))
            #      формирую movable_item
            movable_item = Movable_item(self, card, quantity)

            #      Передаю Inventory_item на новую точку хранения
            new_st_pnt.income(movable_item)
        # else:
        #     # возвращаю отказ в перемещении
        #     pass
        pass

    def calc_balance(self, card):
        # расчитывается остаток ТМЦ карточке
        balance = 0
        for i in self._list_id_move_items:
            if self._dict_move_item[i].get_card() is card:
                balance += self._dict_move_item[i].get_quantity()
        return balance

    def get_list_cards(self):
        # Возвращает список карточек ТМЦ, по которым было дижение на данной точке хранения
        list_id_cards = []
        list_card = []
        for i in self._list_id_move_items:
            list_id_cards.append(self._dict_move_item[i].get_card().get_id())
        for i in frozenset(list_id_cards):
            list_card.append(self._dict_cards[i])
        return list_card

def main():
    dict_move_item = Dict_move_item('')

    dict_cards = Dict_cards()
    dict_cards.add(Card_item('Компьютер', 'DeskTop'))
    dict_cards.add(Card_item('Компьютер', 'Notebook'))
    dict_cards.add(Card_item('Принтер', 'HP Laser Jet 1018'))
    dict_cards.add(Card_item('Картридж', 'HP Q2612L экономичный 12L', ))

    print()
    Show_dict_cards(dict_cards)()

    dict_storage_points = Dict_storage_points()
    dict_storage_points.add(Storage_point('Поставщик', 'Oldi', True, dict_move_item, dict_cards))
    dict_storage_points.add(Storage_point('Поставщик', 'ФЦентр', True, dict_move_item, dict_cards))
    dict_storage_points.add(Storage_point('Склад', 'Г-образная комната', False, dict_move_item, dict_cards))
    dict_storage_points.add(Storage_point('Склад', 'Помещение кроссового оборудования', False, dict_move_item, dict_cards))
    dict_storage_points.add(Storage_point('Цех №3', 'ТМЦ переданные в производство', False, dict_move_item, dict_cards))
    dict_storage_points.add(Storage_point('Списание', 'ТМЦ списанные ', False, dict_move_item, dict_cards))
    dict_storage_points.add(Storage_point('Утилизация', 'ООО \"Инвестиции в будущее\"', True, dict_move_item, dict_cards))

    print()
    Show_dict_storage_points(dict_storage_points)()

    Show_balans_storage_point(dict_storage_points[0])()
    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[0], 5))
    Show_balans_storage_point(dict_storage_points[0])()

    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[1], 5))
    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[2], 5))
    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[3], 5))

    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[0], 5))
    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[1], 5))
    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[2], 5))
    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[3], 5))

    dict_storage_points[1].income(Movable_item(dict_storage_points[1], dict_cards[3], 6))
    dict_storage_points[1].income(Movable_item(dict_storage_points[1], dict_cards[3], 12))
    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[2], 5))

    dict_storage_points[1].flow(dict_storage_points[2], dict_cards[3], 12)
    dict_storage_points[0].flow(dict_storage_points[3], dict_cards[0], 3)

    print()
    Show_balans_storage_point(dict_storage_points[0])()
    Show_balans_storage_point(dict_storage_points[1])()
    Show_balans_storage_point(dict_storage_points[2])()
    Show_balans_storage_point(dict_storage_points[3])()
    Show_balans_storage_point(dict_storage_points[4])()


if __name__ == '__main__':
    main()
