""" Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа. """

s = int(input('Введите сумму: '))
p = int(input('Введите произведение: '))
x = 1
y = 1
if x <= 1000 and y <= 1000:
    x = (s - (s ** 2 - 4 * p))/2
    y = s - x
    if x + y == s and x * y == p:
        print('X = {}, Y = {}'.format(round(x), round(y)))
    else:
        print('Таких чисел нет')