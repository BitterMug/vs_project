"""Introduction tests."""

import unittest
from reakcniRychlosti import introduction


class introductionTest(unittest.TestCase):
    """Test set for function introduction."""

    def test_correct_text(self):
        """Test if correct text is displayed."""
        text = "Welcome, this will test your reaction.\n\nBe ready!"
        self.assertEqual(introduction(), text)
