''' Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.'''


def sum(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return sum(a+1, b-1)
    return sum(a-1, b+1)


a = int(input("Введите целое число a: "))
b = int(input("Введите целое число b: "))

print(sum(a, b))
