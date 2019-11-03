import math
letter1 = float(input("A="))
letter2 = float(input("C="))
letter3 = float(input("N="))
# identify y
if letter1 == letter2:
    if letter2 == letter3:
        result1_1 = (letter1+letter2+letter3)*math.pi/180
        result1 = math.cos(result1_1)
        print("y={0}".format(result1))
    else:
        print(0)

elif letter1 < letter2:
    if letter2 == letter3:
        result1_2 = (letter1*letter2*letter3)*math.pi/180
        result2 = math.cos(result1_2)
        print("y={0}".format(result2))
    elif letter2 < letter3:
        result1_3 = (letter1+letter3)*letter2*math.pi/180
        result3= math.cos(result1_3)
        print("y={0}".format(result3))
    else:
        print(0)

else:
    print(0)

