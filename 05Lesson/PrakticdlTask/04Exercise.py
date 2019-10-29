"""
Python Basic Lesson 05, Exercise 04

Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

20191023 Sikorskiy Yuriy
cs.yury.v@pm.me

"""
dNum = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

fOut = open('04_out.txt', 'w', encoding='UTF-8')
with open('04_in.txt', encoding='UTF-8') as fIn:
    for sLine in fIn:
        lLine = sLine.split(' - ')
        lLine[1] = lLine[1][:-1]
        fOut.writelines(dNum[lLine[0]] + ' - ' + lLine[1] + '\n')

fOut.close()
