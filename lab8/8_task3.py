# s = f3 + f8; fi -- число фібоначчі
i = int(input("i = "))
j = int(input("j = "))


def fib(k):
    if k == 1 or k == 2:
        return 1
    else:
        return fib(k-1) + fib(k-2)


s = fib(i) + fib(j)
print(s)

