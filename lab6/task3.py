# x,y є R**n .Знайти суму векторів

n = int(input('Кількість елементів векторів = '))
x_list = [float(input('Координата векора Х ')) for x in range(n)]
y_list = [float(input('Координата векора Y ')) for x in range(n)]
suma = list(map(lambda x, y: x + y, x_list, y_list))
print("сума векторів x i y = {0}".format(suma))