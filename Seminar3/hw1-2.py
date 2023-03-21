
import random

n = int(input('Введите число: '))
rnd_num = [random.randint(0, 100) for i in range(1, 10)]
print(rnd_num)
temp = 0
closer_num = -1
for i in range(len(rnd_num)):
    min_d = max(rnd_num) - n
    if int(rnd_num[i]) == n:
        temp += 1
for i in set(rnd_num):
    if abs(i - n) < min_d:
        min_d = abs(i - n)
        closer_num = i
print(f' - {temp} раз встречается в списке {n},\n - близкое число {closer_num} ')
