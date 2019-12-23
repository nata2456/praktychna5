#дана цілочислова квадратна матриця
# розмістити елементи парних рядків у порядку зростання
n = int(input('Size of matrix = '))
mat = [[int(input("El {0},{1} = ".format(i, j))) for j in range(n)] for i in range(n)]
print('Original matrix')
for row in mat:
    print(row)

res = []
for row in mat:
    if mat.index(row) % 2 == 0:
        res.append(sorted(row))

    if mat.index(row) % 2 != 0:
        res.append(row)

print('Sorted matrix :  ')
tres = [[res[i][j] for j in range(len(res))] for i in range(len(res))]
for k in tres:
    print(k)