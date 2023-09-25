import unittest
from hypothesis import given, strategies as st  # type: ignore
from main import find_absolute_value, find_difference

class TestMainFunctions(unittest.TestCase):
    @given(st.integers())   # type: ignore
    def test_find_absolute_value(self, num: int) -> None:
        self.assertEqual(find_absolute_value(num), abs(num))
    
    @given(st.integers(), st.integers())    # type: ignore
    def test_find_difference(self, num1: int, num2: int) -> None:
        self.assertEqual(find_difference(num1, num2), num1 - num2)
    
    @given(st.integers(min_value = 1), st.integers(min_value = 1)) # type: ignore
    def test_find_absolute_large_values(self, num1: int, num2: int) -> None:
        result: int = find_absolute_value(find_difference(num1, num2))
        self.assertEqual(result, abs(num1 - num2))
    
    @given(st.integers(min_value = 1), st.integers(min_value = 1)) # type: ignore
    def test_find_difference_large_values_positive(self, num1: int, num2: int) -> None:
        result: int = find_difference(num1, num2)
        self.assertEqual(result, num1 - num2)
    
    @given(st.integers(min_value = -1), st.integers(min_value = -1)) # type: ignore
    def test_find_difference_large_values_negative(self, num1: int, num2: int) -> None:
        result: int = find_difference(num1, num2)
        self.assertEqual(result, num1 - num2)
    
    @given(st.integers(min_value = -1), st.integers(min_value = 1)) # type: ignore
    def test_find_difference_large_values_mixed(self, num1: int, num2: int) -> None:
        result: int = find_difference(num1, num2)
        self.assertEqual(result, num1 - num2)

if __name__ == '__main__':
    unittest.main(verbosity = 2)