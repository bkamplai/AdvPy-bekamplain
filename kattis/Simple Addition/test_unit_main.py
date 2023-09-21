import unittest
from hypothesis import given, strategies as st # type: ignore
from main import is_positive, fits_domain, sum


class TestMain(unittest.TestCase):
    @given(st.integers(min_value=1), st.integers(min_value=1)) # type: ignore
    def test_is_positive(self, num1: int, num2: int) -> None:
        self.assertTrue(is_positive(num1, num2))


    @given(st.integers(max_value=10**10), st.integers(max_value=10**10)) # type: ignore
    def test_fits_domain(self, num1: int, num2: int) -> None:
        self.assertTrue(fits_domain(num1, num2))


    def test_sum_valid_input(self) -> None:
        self.assertEqual(sum("5", "10"), 15)


    def test_sum_invalid_input_negative_numbers(self) -> None:
        self.assertIsNone(sum("-5", "10"))
        self.assertIsNone(sum("-5", "-10"))


    def test_sum_invalid_input_non_numeric(self) -> None:
        with self.assertRaises(ValueError):
            sum("abc", "def")


    def test_sum_invalid_input_mixed_format(self) -> None:
        with self.assertRaises(ValueError):
            sum("5", "xyz")


if __name__ == "__main__":
    unittest.main(verbosity = 2)
