import unittest
from hypothesis import given, strategies as st
from buka import calculate, is_power_of_ten

class TestBuka(unittest.TestCase):
    def test_power_of_ten_multiplication(self) -> None:
        result = calculate("10", "*", "10")
        self.assertEqual(result, 100)

    def test_power_of_ten_addition(self) -> None:
        result = calculate("10", "+", "10")
        self.assertEqual(result, 20)

    def test_non_power_of_ten(self) -> None:
        result = calculate("5", "*", "5")
        self.assertIsNone(result)
        result = calculate("5", "+", "5")
        self.assertIsNone(result)
    
    def test_large_input(self) -> None:
        A = "1" * 101
        B = "2" * 50
        result = calculate(A, "*", B)
        self.assertIsNone(result)

    def test_non_digit_input(self) -> None:
        result = calculate("abc", "*", "10")
        self.assertIsNone(result)
    
    def test_invalid_operand(self) -> None:
        result = calculate("10", "/", "10")
        self.assertIsNone(result)
    
    @given(st.integers(min_value=1, max_value=1000000))
    def test_random_valid_inputs(self, A: int) -> None:
        B = "10"
        result = calculate(str(A), "+", B)
        if is_power_of_ten(A):
            self.assertEqual(result, A + int(B))
        else:
            self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()