import math


class NegativeRadiusError(Exception):
    pass


class Circle:
    def __init__(self, x, y, radius):
        if radius < 0:
            raise NegativeRadiusError("Radius of a circle must be positive")

        self.x = x
        self.y = y
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
