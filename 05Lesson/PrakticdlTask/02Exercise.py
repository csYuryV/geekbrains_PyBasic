"""
Python Basic Lesson 05, Exercise 02

Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.

20191023 Sikorskiy Yuriy
cs.yury.v@pm.me

"""

fObj = open('20191023-171949.txt', encoding='UTF-8')
print(f'В файле {fObj.name} {len(list(fObj))} строк(и, а).')
fObj.seek(0)
for j, s in enumerate(fObj, start=1):
    print(f'В строке {j}: {len(s.split())} слов(о, а) ')

fObj.close()
