"""Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?"""


totalNumber = int(input("Введите сколько журавликов сделали в общем:"))

one = totalNumber // 6
two = totalNumber // 6
three = (one + two) * 2
if totalNumber % 6 == 0:
    print (f'Катя сделала = {three}, Петя сделал = {one}, Сережа сделал = {two}')
else:
    print('Колличество журавликов не делиться')