#   Дана цілочислова прямокутна матриця. Визначити максимальне із чисел, яке
#   зустрічається в даній матриці більше одного разу.

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
