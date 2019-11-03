import datetime

class Show_dict_cards:
    def __init__(self, dict_cards):
        self._dict_cards = dict_cards

    def __call__(self):
        print(f'  {self._dict_cards.get_name()}')
        print('+--------------+-----------------+---------------------------------------------+')
        print('|           id | Категория ТМЦ   | Описание                                    |')
        print('+--------------+-----------------+---------------------------------------------+')
        for key, card_item in self._dict_cards.items():
            print(f'| {card_item.get_id():12} | {card_item.get_name():15} | {card_item.get_description():43} |')
        print('+--------------+-----------------+---------------------------------------------+')

class Show_dict_storage_points:
    def __init__(self, dict_storage_points):
        self._dict_storage_points = dict_storage_points

    def __call__(self):
        print(f'  {self._dict_storage_points.get_name()}')
        print('+--------------+-----------------+---------------------------------------+-----+')
        print('|           id | Наименование    | Описаниея                             |Контр|')
        print('+--------------+-----------------+---------------------------------------+-----+')

        for key, storage_point in self._dict_storage_points.items():
            sprovider = 'Да' if storage_point.get_provider() else 'Нет'
            print(f'| {storage_point.get_id():12} | {storage_point.get_name():15} | {storage_point.get_description():37} | {sprovider:3} |')

        print('+--------------+-----------------+---------------------------------------+-----+')

class Show_balans_storage_point:
    def __init__(self, storage_point):
        self._storage_point = storage_point

    def __call__(self):
        print()
        print(f'Остатки на точке хранения: {self._storage_point.get_name()} ({self._storage_point.get_description()}) (id = {self._storage_point.get_id()})')
        print(f'по состоянию на {datetime.datetime.now()}')
        print('+--------------+-----------------+---------------------------------------------+-------------+')
        print('|           id | Категория ТМЦ   | Описание                                    |     Остаток |')
        print('+--------------+-----------------+---------------------------------------------+-------------+')
        for i in self._storage_point.get_list_cards():
            print(f'| {i.get_id():12} | {i.get_name():15} | {i.get_description():43} |{self._storage_point.calc_balance(i):12} |')
        print('+--------------+-----------------+---------------------------------------------+-------------+')


