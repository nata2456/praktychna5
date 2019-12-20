#  Дано масив (список) елементів цілого типу.
#  Знайти середнє геометричне.

from functools import reduce
import math
count = int(input('введіть число: '))
list1 = [int(input('елементи: ')) for x in range(count)]
mul = reduce(lambda mult, el: mult * el, list1, 1)
geom = math.sqrt(mul)
print(geom)