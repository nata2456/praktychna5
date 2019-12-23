## Task 1

__Дано n дійсних чисел. Знайти середнє арифметиче цих чисел.__

```py n = int(input('n = '))
sum = 0
i = 0
for i in range(n):
    x = float(input('x{0}  '.format(i + 1)))
    sum = sum + x
    arithm = sum/n
print("Результат: {0}".format(arithm))
```

## Task 2
__Побудувати масив А=(ai), елементи якого задаються формулою:__

``` py ai = a(i-2)+a(i-1)/2^(i-1)*a(i-3)
a1= a2=x,a3= y
x,y вводяться з клавіатури
Обчислити кількість елементів масиву А.
x = int(input("x = "))
y = int(input("y = "))
n = int(input("n = "))
z = float(input("z = "))
A = []
a1 = x
a2 = x
a3 = y
count = 0
for i in range(n):
    i = 4
    an = a2 + (a3/2**(i-1)*a1)
    a1 = a2
    a2 = a3
    a3 = an
    A.append(an)
for el in A:
    if el > z:
        count += 1
print("кількість елементів більших за z =  {0}".format(count)
```

## Task 3
__Дано два вектори x,y є R^n. Знайти суму векторів.__


``` py n = int(input('Кількість елементів векторів = '))
x_list = [float(input('Координата векора Х ')) for x in range(n)]
y_list = [float(input('Координата векора Y ')) for x in range(n)]
suma = list(map(lambda x, y: x + y, x_list, y_list))
print("сума векторів x i y = {0}".format(suma))
```

## Task 4 
__Впорядкувати елементи масиву за зростанням__

```py n = int(input('Кількість елементів = '))
num_list = [float(input('Чиcла = ')) for i in range(n)]
for i in range(len(num_list)):
    minimum = i
    for j in range(i + 1, len(num_list)):

        if num_list[j] < num_list[minimum]:
            minimum = j
            num_list[minimum], num_list[i] = num_list[i], num_list[minimum]

print(num_list)
```





