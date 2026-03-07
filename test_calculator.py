import unittest
import math
from Calculator import add, subtract, multiply, divide, square_root, factorial, natural_log, power

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_square_root(self):
        self.assertEqual(square_root(16), 4)
        with self.assertRaises(ValueError):
            square_root(-1)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

    def test_natural_log(self):
        self.assertAlmostEqual(natural_log(math.e), 1)
        with self.assertRaises(ValueError):
            natural_log(0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

if __name__ == '__main__':
    import math
    unittest.main()
