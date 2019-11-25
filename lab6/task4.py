n = int(input('Кількість елементів = '))
num_list = [float(input('Чиcла = ')) for i in range(n)]
new_list = []
for i in range(len(num_list)):
    a = num_list[i]
    j = i

    while (num_list[j-1] > a) and (j > 0):
        num_list[j] = num_list[j-1]
        j = j - 1
        num_list[j] = a
        print(a)




        # num_list[j] = num_list[d]
        # num_list[j] = a
        # print(a)



