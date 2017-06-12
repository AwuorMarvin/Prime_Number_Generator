import unittest
from prime_generator import prime_number_generator

class PrimeGeneratorTest(unittest.TestCase):
    def test_prime_generator_only_takes_integers(self):
        self.assertIsInstance(19, int, msg="The test failed because you passed in a non-int")