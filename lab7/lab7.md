 # Task 1
__Дана цілочислова матриця.
 визначити суму від'ємних елементів з обома парними індексами__

```py 
n = int(input("n = "))
m = int(input("m = "))

matrix = [[int(input("mat[{0}][{1}] = ".format(i,j))) for j in range(m)] for i in range(n)]

sum = 0
for i in range(0, n, 2):
    for j in range(0, m, 2):
        if matrix[i][j] < 0:
            sum += matrix[i][j]

print(sum)
```
## Task2
__Створити програму, для знаходження детермінанта матриці А__
```py 
import copy
def minor(A, i, j):
    M = copy.deepcopy(A)
    del M[i]
    for i in range(len(A[0]) - 1):
        del M[i][j]
    return M

def det(A):
    m = len(A)
    n = len(A[0])
    if m != n:
        return None
    if n == 1:
        return A[0][0]
    signum = 1
    determinant = 0

    for j in range(n):
        determinant += A[0][j] * signum * det(minor(A, 0, j))
        signum *= -1
    return determinant

n = int(input("enter number: "))
A = [[int(input('el:{0},{1}: '.format(i, j)))for j in range (n)]for i in range (n)]


print(det(A))
```
## Task3
__Дана цілочислова квадратна матриця,
розмістити елементи парних рядків у порядку зростання__
```py 
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
```

## Task4
__1. Дана цілочислова прямокутна матриця. Визначити кількість рядків, які не містять жодного нульового елемента.__
```py 
i = int(input('i = '))
j = int(input('j = '))
matrix = [
    [int(input('El ')) for x in range(i)] for y in range(j)
]
for row in matrix:
    print(row)

count_zero = 0
for i in matrix:
    if 0 not in i:
        count_zero += 1
print(count_zero)
```
## Task5
   __Дана цілочислова прямокутна матриця. Визначити максимальне із чисел, яке зустрічається в даній матриці більше одного разу.__

```py 
i = int(input('i = '))
j = int(input('j = '))
matrix = [
    [int(input('El ')) for x in range(i)] for y in range(j)
]
for row in matrix:
    print(row)

num_list = []  # all elements

for row in matrix:
    for col in row:
        num_list.append(col)

res = []  # repetitive elements
for el in num_list:
    if num_list.count(el) > 1:
        res.append(el)
print(max(set(res)))
```