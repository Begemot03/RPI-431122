import math

class Geometric:
    def calculateArea(self):
        print("Calculating area")

class Square(Geometric):
    def __init__(self, a):
        self.side = a

    def _perimeter(self):
        print("Perimeter of Square {}: {}\n".format(self.side, self.side*4))

    def calculateArea(self):
        print("Area of Square {}: {}\n".format(self.side, pow(self.side, 2)))

class Circle(Geometric):
    def __init__(self, r):
        self.__radius = r

    def calculateArea(self):
        area = math.pi * self.__radius**2
        print("Area of Circle with radius {}: {:.2f}".format(self.__radius, area))

geom = Geometric()
geom.calculateArea()

sq = Square(5)
sq.calculateArea()
sq._perimeter()

cir = Circle(3)
cir.calculateArea()

print("Check subclass: ", issubclass(Square, Geometric))
print("Check instance sq->Square: ", isinstance(sq, Square))
print("Check instance sq->Geometric: ", isinstance(sq, Geometric))
print("Check instance sq->dict: ", isinstance(sq, dict))

print("__Geometric bases__: ", Geometric.__bases__)
print("__Square bases__: ", Square.__bases__)