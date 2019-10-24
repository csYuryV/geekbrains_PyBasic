"""
Python Basic Lesson 05, Exercise 03

Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов. Определить, кто из сотрудников
имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить
подсчет средней величины дохода сотрудников.

20191023 Sikorskiy Yuriy
cs.yury.v@pm.me

"""

forbes = []

with open('forbes_src.txt', encoding='UTF-8') as fIn:
    for slice in fIn:
        slice = slice[:-1]
        lLine = slice.split(' | ')
        lLine[2] = lLine[2].split('; ')
        try:
            lLine[0] = int(lLine[0])
        except ValueError:
            print(f'\nВ строке {lLine[1]} ValueError в колонке \'п/п\'\n')
        try:
            lLine[3] = int(lLine[3])
        except ValueError:
            print(f'\nВ строке {lLine[0]} ValueError в колонке \'дохлды\'\n')
        try:
            lLine[4] = int(lLine[4])
        except ValueError:
            print(f'\nВ строке {lLine[0]} ValueError в колонке \'возраст\'\n')
        forbes.append(lLine)

quantity = 0
amountOfIncome = 0
averageIncome = 0
forbesSmaller20 = []

fOut = open('forbes20.txt', 'w', encoding='UTF-8')
print('\nСписок богатейших бизнесменов России (топ 21), чьё состояние менее 20000 млн$\n', file=fOut)
print(' имя фамилия             возраст состояние млн$', file=fOut)
print('+-----------------------+-------+--------------+', file=fOut)
for person in forbes:
    amountOfIncome += person[3]
    quantity += 1
    if person[3] < 20000:
        forbesSmaller20.append(person)
        print(f' {person[1]:20} {person[4]:10} {person[3]:14}', file=fOut)

averageIncome = amountOfIncome / quantity
print(f'\nСредняя величина состояния богатейших бизнесменов России (топ 21)', file=fOut)
print(f'составила {averageIncome:0.2f} млн$', file=fOut)
fOut.close()

with open('forbes20.txt', encoding='UTF-8') as fIn:
    for line in fIn:
        print(line, end='')
