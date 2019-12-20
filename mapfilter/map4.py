#  Дано два вектори (списки з координатами – дійсними числами). Знайти
#  скалярний добуток векторів

v1 = [float(input('Coordinate of vector 1: ')) for x in range(3)]
v2 = [float(input('Coordinate of vector 2: ')) for y in range(3)]
scalar = sum(list(map(lambda x, y: x * y, v1, v2)))

print(scalar)