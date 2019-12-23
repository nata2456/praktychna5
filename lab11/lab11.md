# Лабораторна робота №11
## Task1
__Описати клас, який містить вказані поля і методи.__

|Клас   |Вектор   |        
|---|---|
|Поле   |  1. для зберігання координат вектора             
| Методи|2. введення/виведення елементів вектора; 3. визнчення довжини вектора; 4. нормування вектора; порівняння з іншим вектором;    5. перевантаження операторів +(додавання векторів), -(віднімання векторів), *(знаходження скалярного добутку)  |     
|   | 

```py 
import math
class TVector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, arg):
        self.x = arg

    def x(self):
         return self.x

    def set_y(self, arg):
        self.y = arg

    def y(self):
        return self.x

    def square_length(self):
        return (self.x * self.x) + (self.y * self.y)

    def length(self):
        return math.sqrt(self.square_length())

    def normalize(self):
        length = self.length()
        if length == 0.0:
            return TVector2D(0, 0)
        return TVector2D(self.x / length, self.y / length)

    def __add__(self, vec):
        return TVector2D(self + vec.x, self + vec.y)

    def __sub__(self, vec):
        return TVector2D(self - vec.x, self - vec.y)

    def __and__(self, vec):
        return self.x * vec.x + self.y * vec.y
    def __str__(self):
        return "TVector2D: {0}, {1}".format(self.x, self.y)

v = TVector2D(3,4)
print(v)
print('Length = ', v.length())
print('Normalize = ', v.normalize())


```      
