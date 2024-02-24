from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass


class ShapeWithDimensions(Shape, ABC):
    @abstractmethod
    def set_dimensions(self, *args):
        pass

    @abstractmethod
    def get_dimensions(self):
        pass


class Circle(ShapeWithDimensions):
    def __init__(self, diameter):
        self.diameter = diameter

    def set_dimensions(self, diameter):
        self.diameter = diameter

    def get_dimensions(self):
        return self.diameter

    def get_area(self):
        radius = self.diameter / 2
        return 3.14 * radius * radius


class Rectangle(ShapeWithDimensions):
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def set_dimensions(self, length, height):
        self.length = length
        self.height = height

    def get_dimensions(self):
        return self.length, self.height

    def get_area(self):
        return self.length * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def set_base(self, new_base):
        self.base = new_base

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return 0.5 * self.base * self.height


def main():
    my_circle = Circle(5)
    print(f"The area of the circle is: {my_circle.get_area()}")

    my_rectangle = Rectangle(4, 5)
    my_rectangle.set_dimensions(6, 8)
    print(f"The area of the rectangle is: {my_rectangle.get_area()}")

    my_triangle = Triangle(5, 12)
    my_triangle.set_base(3)
    my_triangle.set_height(24)
    print(f"The area of the triangle is: {my_triangle.get_area()}")


if __name__ == "__main__":
    main()
