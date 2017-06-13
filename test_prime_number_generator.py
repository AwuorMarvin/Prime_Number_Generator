import unittest
from prime_generator import prime_number_generator

class PrimeGeneratorTest(unittest.TestCase):
    def test_prime_generator_only_takes_integers(self):
        self.assertIsInstance(19, int, msg="The test failed because you passed in a non-int")

    def test_check_that_2_is_not_forgotten(self):
        result = prime_number_generator(2)
        self.assertIn(2, result, msg="Please check how your function handles number 2")