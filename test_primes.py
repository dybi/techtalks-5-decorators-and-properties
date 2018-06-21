from unittest import TestCase
from unittest.mock import patch
patch('primes.sleeper').start()
from primes import is_prime


class TestIsPrime(TestCase):
    def test_tahat_seven_is_prime(self):
        result = is_prime(7)

        self.assertEqual(result, True)

    def test_that_four_is_not_prime(self):
        result = is_prime(4)

        self.assertEqual(result, False)
