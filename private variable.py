import math

class Circle:
    __pi = 3.141  # Private class variable

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_list(cls, number_list):
        return cls(number_list[0])

    def area(self):
        return Circle.__pi * self.radius**2

    def perimeter(self):
        return 2 * Circle.__pi * self.radius
        
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Create an instance of the Circle class using class method
circle_instance = Circle.from_list(numbers)

# Calculate and print area and perimeter using instance methods
print("Area:", circle_instance.area())
print("Perimeter:", circle_instance.perimeter())
