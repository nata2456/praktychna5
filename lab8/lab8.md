## Task1
__За даними дійсними числами  a i b обчислити:__
__u = f(a,b)+f(a,2)
f(x,y)={x^3+sqrt(x^2+y^4),x>y
(x^2-2*x+sqrt(x),інакше__

```py 
import math
a = float(input("a = "))
b = float(input("b = "))


def find_f(x, y):
    return (x**3 + math.sqrt(x**2+y**4)) if x > y else (x**2-2*x + math.sqrt(x))/(x**0.6)


u = find_f(a, b) + find_f(2, a) + 2
print(u)
```



## Task2
__Використовуючи підпрограму для знаходження скаларного добуткуб обчислити s = 2<a,b>-2<a,c>__
__a,b,c є R^n,<x,y> скалярний добуток__

```py 
n = int(input("n = "))
la = [float(input('координати а = ')) for i in range(n)]
lb = [float(input('координати b = ')) for j in range(n)]
lc = [float(input('координати c = ')) for k in range(n)]
a_b = list(map(lambda coordinate1, coordinate2: coordinate1 * coordinate2, la, lb))    # a*b
a_c = list(map(lambda coordinate1, coordinate2: coordinate1 * coordinate2, la, lc))    # a*c


def listsum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listsum(numlist[1:])


sum_a_b = listsum(a_b)
sum_a_c = listsum(a_c)
s = (2*sum_a_b) - (3*sum_a_c)
print(s)
```


## Task3
__Використовуючи підпрограму для знаходження n-го числа Фібоначчі.__
__Обчислити значення виразу s = f3 + f5, де fi - і-ве число Фібоначчі__
```py 
i = int(input("i = "))
j = int(input("j = "))


def fib(k):
    if k == 1 or k == 2:
        return 1
    else:
        return fib(k-1) + fib(k-2)


s = fib(i) + fib(j)
print(s)
```

