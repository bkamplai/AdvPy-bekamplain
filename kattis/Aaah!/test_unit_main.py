import unittest
from main import count_a, compare_count_a

class TestMainFunctions(unittest.TestCase):
    def test_both_empty_strings(self):
        result = compare_count_a("", "")
        self.assertEqual(result, "go")

    def test_one_empty_string(self):
        result = compare_count_a("aaahhh", "")
        self.assertEqual(result, "go")

    def test_both_strings_with_no_a(self):
        result = compare_count_a("hhh", "hhh")
        self.assertEqual(result, "go")

    def test_jon_has_more_a(self):
        result = compare_count_a("aaah", "aah")
        self.assertEqual(result, "go")

    def test_doctor_has_more_a(self):
        result = compare_count_a("aah", "aaah")
        self.assertEqual(result, "no")

    def test_equal_number_of_a(self):
        result = compare_count_a("aaah", "aaah")
        self.assertEqual(result, "go")

if __name__ == "__main__":
    unittest.main(verbosity = 2)