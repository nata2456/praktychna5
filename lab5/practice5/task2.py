# variant1
# count of digits in the number
n = float(input("n = "))
count = 0
while n:
    n //= 10
    count += 1
print("count = {0}".format(count))

