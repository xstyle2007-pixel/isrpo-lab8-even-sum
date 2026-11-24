import unittest
from even_sum import sum_even_numbers

class TestSumEvenNumbers(unittest.TestCase):

    def test_positive_and_negative(self):
        self.assertEqual(sum_even_numbers([1, 2, 3, 4, 5, 6]), 12)

    def test_all_even(self):
        self.assertEqual(sum_even_numbers([2, 4, 6, 8]), 20)

    def test_all_odd(self):
        self.assertEqual(sum_even_numbers([1, 3, 5, 7]), 0)

    def test_negative_even(self):
        self.assertEqual(sum_even_numbers([-2, -4, -6]), -12)

    def test_mixed_negative_positive(self):
        self.assertEqual(sum_even_numbers([-2, 1, 4, -6, 3]), -4)

    def test_with_zero(self):
        self.assertEqual(sum_even_numbers([0, 1, 2, 3]), 2)

    def test_empty_list(self):
        self.assertEqual(sum_even_numbers([]), 0)

    def test_single_even(self):
        self.assertEqual(sum_even_numbers([8]), 8)

    def test_single_odd(self):
        self.assertEqual(sum_even_numbers([7]), 0)

    def test_tuple_input(self):
        self.assertEqual(sum_even_numbers((2, 3, 4)), 6)

    def test_not_a_list_raises(self):
        with self.assertRaises(TypeError):
            sum_even_numbers("1234")

    def test_float_element_raises(self):
        with self.assertRaises(TypeError):
            sum_even_numbers([2, 3.5, 4])

    def test_bool_element_raises(self):
        with self.assertRaises(TypeError):
            sum_even_numbers([True, 2, 4])

if __name__ == "__main__":
    unittest.main()
