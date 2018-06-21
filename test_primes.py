from unittest import TestCase
from unittest.mock import patch

from primes import is_prime


class TestIsPrime(TestCase):
    @patch('primes.sleeper')
    def test_tahat_seven_is_prime(self, sleeper_mock):
        result = is_prime(7)

        self.assertEqual(result, True)

    @patch('primes.sleeper')
    def test_that_four_is_not_prime(self, sleeper_mock):
        result = is_prime(4)

        self.assertEqual(result, False)
