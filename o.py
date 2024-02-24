from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

def main():
    radius = 5.0
    side = 4.0
    length = 6.0
    width = 8.0

    circle_instance = Circle(radius)
    circle_area = circle_instance.get_area()
    print(f"Circle Area: {circle_area}")

    square_instance = Square(side)
    square_area = square_instance.get_area()
    print(f"Square Area: {square_area}")

    rectangle_instance = Rectangle(length, width)
    rectangle_area = rectangle_instance.get_area()
    print(f"Rectangle Area: {rectangle_area}")

if __name__ == "__main__":
    main()
