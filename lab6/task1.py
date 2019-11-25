# дано n дійнсних х1,х2,...хчисел. знайти їх середнє значення
n = int(input('n = '))

sum = 0
i = 0
for i in range(n):
    x = float(input('x{0}  '.format(i + 1)))
    sum = sum + x
    arithm = sum/n
print("Результат: {0}".format(arithm))
