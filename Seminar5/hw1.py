''' Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии. '''


def degree(a, b):
    if b == 0:
        return 1
    return a * degree(a, b-1)


a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

print(degree(a, b))
