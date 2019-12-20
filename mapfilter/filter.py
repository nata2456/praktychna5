#  Дано масив (список) елементів цілого типу.
#  Підрахувати кількість елементів юілбших за середнє значеннясереднє арифметичне.
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
