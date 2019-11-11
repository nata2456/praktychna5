# variant1
# a(a+1)...(a+n-1)
a = float(input("a= "))
n = int(input("n= "))
s = 1
for i in range(n):
    s *= (a+i)
print( "s = {0}".format(s))

