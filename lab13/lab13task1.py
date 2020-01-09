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
        return TVector2D(self.x + vec.x, self.y + vec.y)

    def __sub__(self, vec):
        return TVector2D(self.x - vec.x, self.y - vec.y)

    def __and__(self, vec):
        return self.x * vec.x + self.y * vec.y

    def __str__(self):
        return "TVector2D: {0}, {1}".format(self.x, self.y)


class TVector3D(TVector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

<<<<<<< HEAD
    def square_length1(self):
        return super().square_length() + (self.z * self.z)
=======
    def square_length(self):
        return super().square_length() + (self.z*self.z)
>>>>>>> 50e8b8a9e85b8732c7e8f596e03372e954ebf8ea

    def length(self):
        return math.sqrt(self.square_length())

    def normalize(self):
        length = self.length()
        if length == 0.0:
            return TVector3D(0, 0, 0)
        return TVector3D(self.x / length, self.y / length, self.z / length)

    def __add__(self, vec):
        return TVector3D(self.x + vec.x, self.y + vec.y, self.z + vec.z)

    def __sub__(self, vec):
        return TVector3D(self.x - vec.x, self.y - vec.y, self.z - vec.z)

    def __and__(self, vec):
        return self.x * vec.x + self.y * vec.y + self.z * vec.z

    def __str__(self):
        return "TVector3D: {0},{1},{2}".format(self.x, self.y, self.z)


v1 = TVector2D(4, 5)
print(v1)
print('Length = ', v1.length())
print('Normalize = ', v1.normalize())

v = TVector3D(3, 4, 7)
print(v)
<<<<<<< HEAD
print('Length = ', v.length1())
print('Normalize = ', v.normalize1())
=======
print('Length = ', v.length())
print('Normalize = ', v.normalize())
v2 = TVector3D(5,7,8)
print(v2)
res = v + v2
print(res)


>>>>>>> 50e8b8a9e85b8732c7e8f596e03372e954ebf8ea
