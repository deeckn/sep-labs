import unittest
from calculator import Calculator


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.c = Calculator()

    def testNewCalculator(self):                # (1)
        self.assertEqual(self.c.get_accumulator(), 0)

    def testSetGetAcc(self):
        a = 5
        self.c.set_accumulator(a)
        self.assertEqual(self.c.get_accumulator(), a)

    def testAdd(self):
        x = 69
        self.c.add(x)
        self.assertEqual(self.c.get_accumulator(), x)

    def testSubtract(self):
        x = 5
        acc = 5
        diff = 0
        self.c.set_accumulator(acc)
        self.c.subtract(x)
        self.assertEqual(self.c.get_accumulator(), diff)

    def testMultiply(self):
        x = 25
        acc = 5
        product = 125
        self.c.set_accumulator(acc)
        self.c.multiply(x)
        self.assertEqual(self.c.get_accumulator(), product)

    def testDivide(self):
        x = 5
        acc = 125
        quotient = 25
        self.c.set_accumulator(acc)
        self.c.divide(x)
        self.assertEqual(self.c.get_accumulator(), quotient)

    def testInputErrorAdd(self):
        x = "A"
        self.assertRaises(
            TypeError, self.c.add, x)

    def testInputErrorSubtract(self):
        x = "A"
        self.assertRaises(TypeError, self.c.subtract, x)

    def testInputErrorMultiply(self):
        x = "A"
        self.assertRaises(TypeError, self.c.multiply, x)

    def testInputErrorDivide(self):
        x = "A"
        self.assertRaises(TypeError, self.c.divide, x)

    def testZeroDivide(self):
        x = 0
        self.assertRaises(ZeroDivisionError, self.c.divide, x)


if __name__ == "__main__":
    unittest.main()
