# Знайти всі значення у словнику, які є унікальними.
n = int(input('кількість = '))
dctn = {i: input('введіть значення: ') for i in range(n)}
u_value = set(val for dic in dctn for val in dctn.values())
print('не повторюються:', u_value)
