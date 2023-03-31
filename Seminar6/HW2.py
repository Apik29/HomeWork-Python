''' Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума) '''

list_nums1 = '1 6 1 3 2 -4 0 7 9 2 5 1 3 -6 7 2'
list_nums = list_nums1.split()
print(*list_nums)
min1 = int(input("Введите минимум:   "))
max1 = int(input("Введите максимум:   "))
result = []
for i in range(1, len(list_nums)):
    if int(list_nums[i]) > min1 and int(list_nums[i]) < max1:
        result.append(i)

print(result)
