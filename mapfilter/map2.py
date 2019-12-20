#  Дано два вектори (списки з координатами – дійсними числами).
# знайти суму векорів
v1 = [float(input("вектор 1: "))for x in range(3)]
v2 = [float(input("вектор 2: "))for x in range(3)]
resv = list(map(lambda x, y: x+y, v1, v2))
print(resv)

