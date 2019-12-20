#  Дано два вектори (списки з координатами – дійсними числами).
#  Зясувати, чи є вектори перпендикулярними.
v1 = [float(input('вектор 1: ')) for x in range(3)]
v2 = [float(input('вектор 2: ')) for y in range(3)]
res = sum(list(map(lambda x, y: x * y, v1, v2)))
print(res)
if sum == 0:
    print('перпендикулярні')
else:
    print('ні')
