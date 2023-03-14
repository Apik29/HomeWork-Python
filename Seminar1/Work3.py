""" Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета."""

num = int(input("Введи шестизначный номер Вашего билета:"))
if num < 100000 or num > 999999:
    print("Вы ввесли не шестизначный номер билета")

else:
    num1 = int(num/100000)
    num2 = int(num/10000) % 10
    num3 = int(num/1000) % 10
    num4 = int(num/100) % 10
    num5 = int(num/10) % 10
    num6 = num % 10

    sum1 = num1 + num2 + num3
    sum2 = num4 + num5 + num6
    if sum1 == sum2:
        print("Ваш билет счастливый :)")
    else:
        print("К сожалению Ваш билет не счастливый :( ")