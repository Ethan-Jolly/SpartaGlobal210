import unittest
from simple_calc import *


class TestCalculator(unittest.TestCase):
    def test_add(self):
        result = add(2, 2)
        self.assertEqual(result, 4)

    def test_subtract(self):
        result = subtract(4, 2)
        self.assertEqual(result, 2)

    def test_multiply(self):
        result = multiply(2, 2)
        self.assertEqual(result, 4)

    def test_divide(self):
        result = divide(6, 2)
        self.assertEqual(result, 3)

    def test_add_params(self):
        test_cases = [(2, 2, 4), (5, 5, 10)]
        for num1, num2, expected in test_cases:
            with self.subTest(num1=num1, num2=num2, expected=expected):
                self.assertEqual(num1, num2, expected)


if __name__ == '__main__':
    unittest.main()
