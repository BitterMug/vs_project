""""Get equation tests."""

import unittest
from reakcniRychlosti import get_equation


class get_equationTest(unittest.TestCase):
    """Test set for function get_equation."""

    def test_positive(self):
        """Test correct positive equation formating."""
        self.assertEqual(get_equation(7, 4, '+'), "7 + 4")

    def test_mostly_positive(self):
        """Test correct mostly positive equation formating."""
        self.assertEqual(get_equation(7, -4, '/'), "7 / -4")

    def test_mostly_positive_reverse(self):
        """Test correct mostly positive equation formating."""
        self.assertEqual(get_equation(-7, 4, '-'), "-7 - 4")

    def test_negative(self):
        """Test correct negative equation formating."""
        self.assertEqual(get_equation(-7, -4, '*'), "-7 * -4")
