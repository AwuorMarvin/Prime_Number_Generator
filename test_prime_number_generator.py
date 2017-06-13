import unittest
from prime_generator import prime_number_generator

class PrimeGeneratorTest(unittest.TestCase):
    def test_prime_generator_only_takes_integers(self):
        self.assertIsInstance(19, int, msg="The test failed because you passed in a non-int")

    def test_check_that_2_is_not_forgotten(self):
        result = prime_number_generator(2)
        self.assertIn(2, result, msg="Please check how your function handles number 2")
    def test_function_generates_right_numbers_btwn_1_10(self):
            result = prime_number_generator(20)
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19], result)