# variant1
# xi = x(i-1) + 2*i
i = int(input("n = "))

x0 = 1

if i == 0:
    print(1)
else:
    for j in range(i-(i-1)):
           xi = x0 + 2*i
           x0 = xi
           print("x(i) = {0}".format(xi))


