with open('text1.txt') as file:
    numbers = []
    for el in file:
        numbers.append(float(el))
    max_el = max(numbers)
    print(max_el)