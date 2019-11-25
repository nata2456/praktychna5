# a1 = a2 = x, a3 = y, ai = a(i-2)+a(i-1)/2**(i-1)*a(i-3),i= 4,..,n
# вивести кількість елементів масиву А більших за число введене з клавіатури z
x = int(input("x = "))
y = int(input("y = "))
n = int(input("n = "))
z = float(input("z = "))
A = []
a1 = x
a2 = x
a3 = y
count = 0
for i in range(n):
    i = 4
    an = a2 + (a3/2**(i-1)*a1)
    a1 = a2
    a2 = a3
    a3 = an
    print(an)
    A.append(an)
for el in A:
    if el > z:
        count += 1
print("кількість елементів більших за z =  {0}".format(count))



