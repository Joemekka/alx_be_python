import unittest
from math_tools import add, devide


class TestMathTools(unittest.TestCase):

    def test_add(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_devide(self):
        with self.assertRaises(ValueError):
            devide(10, 0)

    def setUp(self):
        self.numbers = [1, 2, 3]

    def tearDown(self):
        pass

    def test_sum(self):
        self.assertEqual(sum(self.numbers), 6)


if __name__ == "__main__":
    unittest.main()
