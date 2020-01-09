# Побудувати матрицю А, елементи якої задаються формулою:
# a[i][j] = 1*2*3*j,якщо i*j парне,інакше- 1+2+3+і,і = 1,n ;j = 1,m
## Побудувати одновимірний масив(переписати матрицю в одновимірний масив)

n = int(input('count of rows'))
m = int(input('count of cols'))


def find_j(j):
    mul = 1
    for j in range(1, j + 1):
        mul = j * mul
    return mul


def find_i(i):
    sum = 0
    for i in range(1, i + 1):
        sum += i
    return sum


A = [

    [find_j(j) if (i * j) % 2 == 0 else find_i(i) for j in range(1, m + 1)
     ] for i in range(1, n + 1)

]

print(A)
res = []
for q in range(len(A)):
    for w in range(len(A)):
        res.append(A[q][w])
print(res)
