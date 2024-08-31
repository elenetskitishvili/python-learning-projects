import math

# Base Class


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return None


# Subclasses for Rectangle and Circle


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return round(self.width * self.height, 2)


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

# Function to demonstrate polymorphism


def print_area(shape):
    print(f"The area of the {shape.name} is: {shape.area()}")


# Instantiate Rectangle and Circle
rectangle = Rectangle("Rectangle", 5, 8)
circle = Circle("Circle", 2)

# Call print_area for each shape
print_area(rectangle)
print_area(circle)
