" variant1 "
" xi = x(i-1) + 2*i"
" n = int(input(""))"
n = int(input("n = "))
i = 1
x0 = 1
while i <= n:
    xi = x0 + i * 2
    x0 = xi
    i += 1


print("x(i) = {0}".format(xi))


