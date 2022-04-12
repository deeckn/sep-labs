import hex
import unittest


class KnownValues(unittest.TestCase):
    KnownValues = ((170, "AA"),
                   (160, "A0"),
                   (150, "96"),
                   (140, "8C"),
                   (130, "82"),
                   (120, "78"),
                   (110, "6E"),
                   (100, "64"),
                   (90, "5A"))

    def test_hex_known_values(self):
        for input, output in self.KnownValues:
            result = hex.toHex(input)
            self.assertEqual(result, output)


class CheckInput(unittest.TestCase):
    def test_not_int(self):
        """Raises an InvalidArgument exception when the input is not a positive integer"""
        self.assertRaises(hex.InvalidArgument, hex.toHex, "Test")

    def test_not_positive(self):
        """Raises an InvalidArgument exception when the input is not a positive integer"""
        self.assertRaises(hex.InvalidArgument, hex.toHex, -1)


class CheckOutput(unittest.TestCase):
    def test_output(self):
        """ Output should be uppercase"""
        for integer in range(1, 4000):
            numeral = hex.toHex(integer)
            self.assertEqual(numeral, numeral.upper())


if __name__ == "__main__":
    unittest.main()
