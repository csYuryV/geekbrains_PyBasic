"""
Python Basic Lesson 05, Exercise 06

Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки,
также добавить ее в словарь (со значением убытков).
Пример списка: [{‘firm_1’: 5000, ‘firm_2’: 3000, ‘firm_3’: 1000}, {‘average_profit’: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Подсказка: использовать менеджер контекста.


20191024 Sikorskiy Yuriy
cs.yury.v@pm.me

"""
import json

with open('07listFirm.txt', 'r', encoding='utf-8') as fIn:
    allProfit = []
    allFirms = []
    dallFirmProfit = {}
    for sLine in fIn:
        sline = sLine[:-1]
        lLine = sLine.split()
        try:
            lLine[2] = int(lLine[2])
            lLine[3] = int(lLine[3])
        except ValueError:
            print('Некоректные данные в исходном файле')
            exit()
        profit = lLine[2] - lLine[3]
        lLine.append(profit)
        dallFirmProfit[f'{lLine[1]} \'{lLine[0]}\''] = profit
        if profit > 0:
            # Прибыль
            allProfit.append(profit)

averageProfit = sum(allProfit) / len(allProfit)
dAverageProfit = {}
dAverageProfit['average_profit'] = averageProfit
result = [dallFirmProfit, dAverageProfit]

with open("my_file.json", 'w', encoding='utf-8') as fOut:
    json.dump(result, fOut)
