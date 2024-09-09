class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        # your code here
        self.radius = radius
    def get_radius(self):
        """ Returns the radius of self """
        # your code here
        return self.radius
    def __add__(self, c):
        """ c is a Circle object 
        Returns a new Circle object whose radius is 
        the sum of self and c's radius """
        # your code here
        return Circle(self.radius + c.radius) 

    def __str__(self):
        """ A Circle's string representation is the radius """
        # your code here
        return (f"{self.radius}")

circle = Circle(5)
circle1 = Circle(6)
print(circle + circle1)