# Define a class named Calculator that takes a number as an argument during initialization.
# The class should have two methods: square() and cube(), which print the square and cube of the number respectively.

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square of {self.n} is {self.n ** 2}")

    def cube(self):
        print(f"The cube of {self.n} is {self.n ** 3}")
    
a = Calculator(4)
a.square()
a.cube()