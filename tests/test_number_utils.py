"""Tests for number_utils module."""
import unittest
from number_utils import characteristic, mantissa


class TestCharacteristic(unittest.TestCase):
    """Tests for the characteristic function."""

    def test_valid_positive_integers(self):
        self.assertEqual(characteristic("42"), (True, 42))
        self.assertEqual(characteristic("0"), (True, 0))
        self.assertEqual(characteristic("100"), (True, 100))

    def test_valid_decimals(self):
        self.assertEqual(characteristic("3.14"), (True, 3))
        self.assertEqual(characteristic("2.99"), (True, 2))
        self.assertEqual(characteristic("0.5"), (True, 0))

    def test_valid_negative_numbers(self):
        self.assertEqual(characteristic("-3.14"), (True, -3))
        self.assertEqual(characteristic("-1"), (True, -1))
        self.assertEqual(characteristic("-0.1"), (True, 0))


class TestMantissa(unittest.TestCase):
    """Tests for the mantissa function."""

    def test_valid_decimals(self):
        self.assertEqual(mantissa("3.14"), (True, 14, 100))
        self.assertEqual(mantissa("0.5"), (True, 5, 10))
        self.assertEqual(mantissa("2.001"), (True, 1, 1000))

    def test_integers_no_fractional_part(self):
        self.assertEqual(mantissa("42"), (True, 0, 1))
        self.assertEqual(mantissa("0"), (True, 0, 1))

    def test_invalid_inputs(self):
        self.assertEqual(mantissa(""), (False, 0, 0))
        self.assertEqual(mantissa("abc"), (False, 0, 0))
        self.assertEqual(mantissa(None), (False, 0, 0))


if __name__ == "__main__":
    unittest.main()
