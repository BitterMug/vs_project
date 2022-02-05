"""Init tests."""

import unittest
from reakcniRychlosti import init


class initTest(unittest.TestCase):
    """Test set for init function."""

    def test_correct_values(self):
        """Test if correct values are set."""
        correct = [None, None, None, None, None]
        correct_max = 10
        correct_min = -10
        correct_symbols = "+-*/"
        correct_message = "Answer:"
        cycles, results, times, min, max, symbols, message = init()
        self.assertEqual(results, correct)
        self.assertEqual(times, correct)
        self.assertEqual(min, correct_min)
        self.assertEqual(max, correct_max)
        self.assertEqual(symbols, correct_symbols)
        self.assertEqual(message, correct_message)
