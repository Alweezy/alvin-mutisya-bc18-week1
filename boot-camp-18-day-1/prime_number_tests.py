from unittest import TestCase
from prime_numbers import is_prime, collect_prime_numbers


class PrimeNumberTests(TestCase):
    """Check if prime number generator outputs prime numbers"""
    def test_if_number_is_prime(self):
        self.assertEqual(is_prime(1), False)

    def test_if_number_is_prime2(self):
        self.assertEqual(is_prime(7), True)


class OutPutTests(TestCase):
    """test if output is correct"""
    def test_prime_numbers_correct(self):
        self.assertEqual(collect_prime_numbers(13), [2, 3, 5, 7, 11, 13])

    def test_prime_numbers_correct2(self):
        self.assertEqual(collect_prime_numbers(2), [2])

    def test_number_included_if_prime(self):
        self.assertEqual(collect_prime_numbers(5), [2, 3, 5])

    def test_input_is_not_string(self):
        self.assertEqual(collect_prime_numbers(''), 'Only integers allowed')

    def test_input_is_not_dictionary(self):
        self.assertEqual(collect_prime_numbers({}), 'Only integers allowed')

    def test_input_is_not_tuple(self):
        self.assertEqual(collect_prime_numbers((1,)), 'Only integers allowed')
