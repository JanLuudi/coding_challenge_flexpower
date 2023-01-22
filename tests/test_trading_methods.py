import unittest

from src.trading_methods import compute_total_buy_volume


class TestTradingMethods(unittest.TestCase):
    """
    Perform automated tests.

    Args:
        unittest (_type_): testcase
    """

    def test_compute_total_buy_volume(self) -> None:
        """
        Test, if total buy volume is calculated correctly.
        total_buy_volume in the trades.sqlite dataset is 380 €
        (Not a good test, but I wanted to show, that I know how to structure and write test cases)
        """
        self.assertEqual(compute_total_buy_volume(), 380.0)
