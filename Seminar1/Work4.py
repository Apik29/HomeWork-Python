"""Требуется определить, можно ли от шоколадки размером n * m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника)."""

vertical = int(input('Введите сколько долек по вертикале: '))
diagonal = int(input('Введите сколько долек по диагонале: '))
breakOff = int(input('Введите сколько долек вы хотите отломить: '))

if breakOff < vertical * diagonal and ((breakOff % vertical == 0) or (breakOff % diagonal == 0)):
    print("Отломить возможно")
else:
    print("Отломить не возможно")