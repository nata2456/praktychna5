## Task 1
__Дано масив (список) елементів цілого типу.
Підрахувати кількість елементів юілбших за середнє значеннясереднє арифметичне.__
```py 
from functools import reduce
count = int(input('кількість : '))
list1 = [int(input('елементи: ')) for el in range(count)]
suma = reduce(lambda suma, el: suma + el, list1, 0)
a = suma / len(list1)
print(a)
count2 = 0
for el in list1:
    if el > a:
        count += list1.count(el)
print(count2)
```

## Task 2 
 __Дано два вектори (списки з координатами – дійсними числами).
 Зясувати, чи є вектори перпендикулярними.__
```py
v1 = [float(input('вектор 1: ')) for x in range(3)]
v2 = [float(input('вектор 2: ')) for y in range(3)]
res = sum(list(map(lambda x, y: x * y, v1, v2)))
print(res)
if sum == 0:
    print('перпендикулярні')
else:
    print('ні')

```
## Task 3
__Дано два вектори (списки з координатами – дійсними числами).
Знайти суму векорів__
```py
v1 = [float(input("вектор 1: "))for x in range(3)]
v2 = [float(input("вектор 2: "))for x in range(3)]
resv = list(map(lambda x, y: x+y, v1, v2))
print(resv)
```
## Task 4
 __Дано масив (список) елементів цілого типу.
Знайти середнє геометричне.__

```py
from functools import reduce
import math
count = int(input('введіть число: '))
list1 = [int(input('елементи: ')) for x in range(count)]
mul = reduce(lambda mult, el: mult * el, list1, 1)
geom = math.sqrt(mul)
print(geom)
```
## Task 5
__Дано два вектори (списки з координатами – дійсними числами). Знайти
скалярний добуток векторів__

```py
v1 = [float(input('Coordinate of vector 1: ')) for x in range(3)]
v2 = [float(input('Coordinate of vector 2: ')) for y in range(3)]
scalar = sum(list(map(lambda x, y: x * y, v1, v2)))

print(scalar)
```