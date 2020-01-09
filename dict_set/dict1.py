# знайти значення ключа, яке є у обох словниках одночасно

n = int(input('кількість = '))
dctn1 = {i: input('введіть значення: ') for i in range(n)}
dctn2 = {i: input('введіть значення: ') for i in range(n)}
for (key, value) in set(dctn1.items()) & set(dctn2.items()):
    print("{0}:{1} є у обох словниках".format(key, value))
