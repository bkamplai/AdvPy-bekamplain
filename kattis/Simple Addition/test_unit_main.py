import unittest
from main import is_positive, fits_domain, sum

class TestMain(unittest.TestCase):
    def test_is_positive(self):
        self.assertTrue(is_positive(5, 10))
        self.assertTrue(is_positive(0.1, 0.01))
        self.assertFalse(is_positive(-5, -10))
        self.assertFalse(is_positive(-0.1, -0.01))
        self.assertFalse(is_positive(5, -10))
        self.assertFalse(is_positive(-5, 10))
    
    def test_fits_domain(self):
        self.assertTrue(fits_domain(9999999999, 9999999999))
        self.assertFalse(fits_domain(10**10000, 10**10000))

    def test_sum_valid_input(self):
        self.assertEqual(sum("5", "10"), 15)
    
    def test_sum_invalid_input_negative_numbers(self):
        self.assertIsNone(sum("-5", "10"))
        self.assertIsNone(sum("-5", "-10"))
    
    def test_sum_invalid_input_non_numeric(self):
        with self.assertRaises(ValueError):
            sum("abc", "def")
    
    def test_sum_invalid_input_mixed_format(self):
        with self.assertRaises(ValueError):
            sum("5", "xyz")

if __name__ == "__main__":
    unittest.main(verbosity = 2)