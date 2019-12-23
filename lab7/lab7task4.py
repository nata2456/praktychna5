# 1. Дана цілочислова прямокутна матриця. Визначити кількість рядків, які не містять
# жодного нульового елемента.
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
