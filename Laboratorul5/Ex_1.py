# Create a class hierarchy for shapes, starting with a
# base class Shape. Then, create subclasses like Circle,
# Rectangle, and Triangle.
# Implement methods to calculate area and perimeter for each shape.
import math
class Shape:
    def area(self): pass

    def perimeter(self): pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.width + self.length)


class Triangle(Shape):
    def __init__(self, sideA, sideB, sideC):
        self.sideA = sideA
        self.sideB = sideB
        self.sideC = sideC

    def area(self):
        a = (self.sideA + self.sideB + self.sideC) / 2
        return math.sqrt(a * (a - self.sideA) * (a - self.sideB) * (a - self.sideC))

    def perimeter(self):
        return self.sideA + self.sideB + self.sideC


def main():
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 4, 5)

    print("Circle -> Area:", circle.area(), "Perimeter:", circle.perimeter())
    print("Rectangle -> Area:", rectangle.area(), "Perimeter:", rectangle.perimeter())
    print("Triangle -> Area:", triangle.area(), "Perimeter:", triangle.perimeter())


main()
