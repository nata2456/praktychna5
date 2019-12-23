# дана цілочислова матриця.
# визначити суму від'ємних елементів з обома парними індексами

n = int(input("n = "))
m = int(input("m = "))

matrix = [[int(input("mat[{0}][{1}] = ".format(i,j))) for j in range(m)] for i in range(n)]

sum = 0
for i in range(0, n, 2):
    for j in range(0, m, 2):
        if matrix[i][j] < 0:
            sum += matrix[i][j]

print(sum)
