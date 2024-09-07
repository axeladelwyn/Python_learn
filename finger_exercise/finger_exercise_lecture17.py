class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        # your code here
        self.rad = radius

    def get_radius(self):
        """ Returns the radius of self """
        # your code here
        return self.rad

    def set_radius(self, radius):
        """ radius is a number
        Changes the radius of self to radius """
        # your code here
        self.rad = radius
    def get_area(self):
        """ Returns the area of self using pi = 3.14 """
        # your code here
        pi = 3.14
        return pi * (self.rad ** 2)
    def equal(self, c):
        """ c is a Circle object
        Returns True if self and c have the same radius value """
        # your code here
        return self.rad == c.get_radius()

    def bigger(self, c):
        """ c is a Circle object
        Returns self or c, the Circle object with the bigger radius """
        # your code here
        if self.rad > c.get_radius():
            return self
        else:
            return c

circle = Circle(50)
circle12 = Circle(100)
# print(circle.set_radius(30))
equal = circle.equal(circle)
print(equal)
print(circle12.get_radius())
bigger_circle = circle.bigger(circle12)
print(f"The bigger circle has a radius of: {bigger_circle.get_radius()}")


class Int_set(object):
    def __init__(self):
        self._vals = []
    def insert(self, e):
        if e not in self._vals:
            self._vals.append(e)

    def member(self, e):
        return e in self._vals
    
    def remove(self, e):
        try:
            self._vals.remove(e)
        except:
            raise ValueError(f"{str(e)} not found")

    def get_members(self):
        return self._vals[:]