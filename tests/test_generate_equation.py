"""Generate equation tests."""

import unittest
from reakcniRychlosti import generate_equation


class generate_equationTest(unittest.TestCase):
    """Test set for function generate_equation."""

    def test_correct_values(self):
        """Test if correct values are generated."""
        min, max, symbols = -20, 30, "+-*/"
        a, b, symbol = generate_equation(min, max, symbols)
        self.assertTrue(min <= a, a <= max)
        self.assertTrue(min <= b, b <= max)
        self.assertTrue(symbols.__contains__(symbol))
