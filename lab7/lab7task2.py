# створити програму, для знаходження детермінанта матриці А
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
