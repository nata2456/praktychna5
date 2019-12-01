# s = 2*<a,b>-3*<a,c>; a,b,c є R^n; <x,y> скаларний добуток
n = int(input("n = "))
la = [float(input('координати а = ')) for i in range(n)]
lb = [float(input('координати b = ')) for j in range(n)]
lc = [float(input('координати c = ')) for k in range(n)]
a_b = list(map(lambda coordinate1, coordinate2: coordinate1 * coordinate2, la, lb))    # a*b
a_c = list(map(lambda coordinate1, coordinate2: coordinate1 * coordinate2, la, lc))    # a*c


def listsum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listsum(numlist[1:])


sum_a_b = listsum(a_b)
sum_a_c = listsum(a_c)
s = (2*sum_a_b) - (3*sum_a_c)
print(s)


