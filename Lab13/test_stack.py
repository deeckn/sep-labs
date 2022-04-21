import unittest
from stack import Stack


class StackTest(unittest.TestCase):
    def setUp(self):
        self.s = Stack()

    def testNewStack(self):
        self.assertTrue(self.s.isEmpty())
        self.assertEqual(self.s.size(), 0)

    def testPushes(self):
        nPushes = 6
        for i in range(nPushes):
            self.s.push("item")

        self.assertFalse(self.s.isEmpty())
        self.assertEquals(self.s.size(), nPushes)

    def testPushPop(self):
        size = self.s.size()

        item = "Python"
        self.s.push(item)
        self.assertEqual(self.s.pop(), item)
        self.assertEqual(self.s.size(), size)


if __name__ == "__main__":
    unittest.main(verbosity=2)
