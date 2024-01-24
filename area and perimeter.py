import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_list(cls, number_list):
        # Assuming the first element in the list is the radius
        return cls(number_list[0])

    @staticmethod
    def area(radius):
        return math.pi * radius**2

    @staticmethod
    def perimeter(radius):
        return 2 * math.pi * radius

numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Create an instance of the Circle class using class method
circle_instance = Circle.from_list(numbers)

# Calculate and print area and perimeter using static methods
print("Area:", Circle.area(circle_instance.radius))
print("Perimeter:", Circle.perimeter(circle_instance.radius))
