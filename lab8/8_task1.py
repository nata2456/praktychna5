# u = f(a,b) + f(a,2)+2
# x^3 + (x^2+y^4), x>y; інакше
# (x^2-2*x+x^(1/2))/x^(3/5)
import math
a = float(input("a = "))
b = float(input("b = "))


def find_f(x, y):
    return (x**3 + math.sqrt(x**2+y**4)) if x > y else (x**2-2*x + math.sqrt(x))/(x**0.6)


u = find_f(a, b) + find_f(2, a) + 2
print(u)