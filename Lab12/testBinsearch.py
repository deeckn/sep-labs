import binsearch
import unittest


class KnowValues(unittest.TestCase):
    known_values = ((([1, 2, 3, 4], 1), 0),
                    (([1, 2, 3, 4], 2), 1),
                    (([1, 2, 3, 4], 3), 2),
                    (([1, 2, 3, 4], 4), 3),
                    (([2, 3, 4, 5], 2), 0),
                    (([2, 3, 4, 5], 3), 1),
                    (([2, 3, 4, 5], 4), 2),
                    (([2, 3, 4, 5], 5), 3),
                    (([3, 4, 5, 6, 7], 3), 0),
                    (([3, 4, 5, 6, 7], 4), 1),
                    (([3, 4, 5, 6, 7], 5), 2),
                    (([3, 4, 5, 6, 7], 6), 3),
                    (([3, 4, 5, 6, 7], 7), 4),
                    (([5, 2, 3, 1], 4), None))

    def test_bin_search(self):
        for input, output in self.known_values:
            result = binsearch.binsearch(input[0], input[1])
            self.assertEqual(result, output)


class SanityCheck(unittest.TestCase):
    def check_in_range(self):
        list = [1, 2, 3, 4]
        i = binsearch.binsearch(list, 3)
        size = len(list)
        self.assertTrue(i < size)

    def check_answer(self):
        list = [1, 2, 3, 4]
        i = binsearch.binsearch(list, 3)
        self.assertEqual(list[i], 3)

    def check_none(self):
        list = [1, 2, 3, 4]
        i = binsearch.binsearch(list, 10)
        self.assertEqual(None, i)


class BinIncorrectInput(unittest.TestCase):
    def test_not_list(self):
        self.assertRaises(binsearch.InvalidArgument,
                          binsearch.binsearch, {1, 2, 3}, 3)


if __name__ == "__main__":
    unittest.main()
