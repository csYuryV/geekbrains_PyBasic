"""
Python Basic Lesson 05, Exercise 06

Необходимо создать (не программно) текстовый файл, где каждая строка описывает
учебный предмет и наличие лекционных, практических и лабораторных занятий по этому
предмету и их количество. Важно, чтобы для каждого предмета не обязательно были
все типы занятий. Сформировать словарь, содержащий название предмета и общее
количество занятий по нему. Вывести словарь на экран.

20191024 Sikorskiy Yuriy
cs.yury.v@pm.me

"""

with open('06listTraining.txt', encoding='UTF-8') as fIn:
    dCourses = {}
    for sLine in fIn:
        sLine = sLine[:-1]
        lLine = sLine.split(' | ')
        lLine[1] = lLine[1].split()
        ocupations = {}
        iCuntOfCourses = 0
        for sOccupation in lLine[1]:
            lOccupation = sOccupation.split(':')
            try:
                ocupations[lOccupation[0]] = int(lOccupation[1])
                iCuntOfCourses += ocupations[lOccupation[0]]
            except ValueError:
                print('Некорректные данные в файле, будут проигнорированы')
        lLine[1] = ocupations
        dCourses[str(lLine[0])] = iCuntOfCourses
        print(lLine)

print('\nСловарь-результат:\n', dCourses, sep='')



