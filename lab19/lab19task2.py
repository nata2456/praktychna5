# Дано типізваний файл, кий містить цілі числа.
# Визначити кількість непарних елементів, використавши
# динаміний масив для збереження елементів.
# Непарні елементи зберегти у файлі <NP.dat>, дотримуючись порядку їх
# слідування у даному типізованому файлі.
with open('num.txt') as file:
    with open('NP.dat', 'wb')as file2:
        numbers = []
        str = ''
        count = 0
        for el in file:
            numbers.append(int(el))
        for e in numbers:
            if e % 2 == 0:
                count += 1
            else:
                file2.write(bytes(e))

print(count)


