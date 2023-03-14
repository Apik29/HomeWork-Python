#Найдите сумму цифр трехзначного числа.

number = int(input("Введите трехзначное число: "))
one = number % 10
two = number // 10 % 10
three = number // 100
summ = one + two + three
print(" сумма цифр = ", summ)