import unittest
from circle import Circle, InputTypeError
import math


class CircleTest(unittest.TestCase):
    def setUp(self):
        self.c = Circle(1, 2, 3)

    def testAttribute(self):
        self.assertTrue(isinstance(self.c.x, int)
                        or isinstance(self.c.x, float))
        self.assertTrue(isinstance(self.c.y, int))
        self.assertTrue(isinstance(self.c.radius, int))

    def checkRadius(self):
        self.assertLess(0, self.c.radius)

    def testGetArea(self):
        area = math.pi*3*3
        self.assertEqual(area, self.c.get_area())

    def testGetPerimeter(self):
        perimeter = math.pi*2*3
        self.assertEqual(perimeter, self.c.get_perimeter())

    def testMove(self):
        self.c.move(2, 3)
        self.assertEqual(self.c.x, 2)
        self.assertEqual(self.c.y, 3)

    def testInputMove(self):
        self.assertRaises(InputTypeError, self.c.move, "s", "s")


if __name__ == "__main__":
    unittest.main()
