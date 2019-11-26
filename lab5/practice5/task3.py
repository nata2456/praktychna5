# variant1
import math

epsilon = float(input("epsilon = "))
x = float(input("x = "))
suma = 2
f = 1
n = 1
while True:
    result = abs((1/f)*((x-1)/(x+1))**(2*n-1))
    if result >= epsilon:
        suma += result
        n += 1
        f *= (2*n-1)
    else:
        break
print("result = {0} ".format(suma))
