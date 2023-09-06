import unittest
from buka import calculate

class TestBuka(unittest.TestCase):
    def test_power_of_ten_multiplication(self):
        result = calculate("10", "*", "10")
        self.assertEqual(result, 100)

    def test_power_of_ten_addition(self):
        result = calculate("10", "+", "10")
        self.assertEqual(result, 20)

    def test_non_power_of_ten(self):
        result = calculate("5", "*", "5")
        self.assertIsNone(result)
        result = calculate("5", "+", "5")
        self.assertIsNone(result)
    
    def test_large_input(self):
        A = "1" * 101
        B = "2" * 50
        result = calculate(A, "*", B)
        self.assertIsNone(result)

    def test_non_digit_input(self):
        result = calculate("abc", "*", "10")
        self.assertIsNone(result)
    
    def test_invalid_operand(self):
        result = calculate("10", "/", "10")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()