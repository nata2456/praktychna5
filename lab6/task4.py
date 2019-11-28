n = int(input('Кількість елементів = '))
num_list = [float(input('Чиcла = ')) for i in range(n)]
for i in range(len(num_list)):
    minimum = i
    for j in range(i + 1, len(num_list)):

        if num_list[j] < num_list[minimum]:
            minimum = j
            num_list[minimum], num_list[i] = num_list[i], num_list[minimum]

print(num_list)


