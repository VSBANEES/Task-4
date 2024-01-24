class Circle:
    def __init__(self, number_list):
        self.number_list = number_list

# Example usage:
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Create an instance of the Circle class
circle_instance = Circle(numbers)

# Access the list attribute within the instance
print("List in Circle instance:", circle_instance.number_list)
