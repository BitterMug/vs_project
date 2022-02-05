import unittest
from reakcniRychlosti import evaluate


class evaluateTest(unittest.TestCase):

    def test_correct(self):
        """Test if correct values returned."""
        self.assertEqual(evaluate(4, -3, "*", -12), True)

    def test_false(self):
        """Test if correct values returned."""
        self.assertEqual(evaluate(4, -3, "-", 8), False)
