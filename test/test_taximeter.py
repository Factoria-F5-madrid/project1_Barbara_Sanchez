import unittest
from datetime import time
from fee import get_dynamic_prices
from taximeter import total_price

class TestFeeLogic(unittest.TestCase):
    def test_peak_morning(self):
        precio = get_dynamic_prices(time(8, 0))
        self.assertEqual(precio, (0.03, 0.07))

    def test_peak_afternoon(self):
        precio = get_dynamic_prices(time(17, 30))
        self.assertEqual(precio, (0.03, 0.07))

    def test_off_peak(self):
        precio = get_dynamic_prices(time(3, 0))
        self.assertEqual(precio, (0.02, 0.05))

class TestCalculation(unittest.TestCase):
    def test_total_price(self):
        move_time = 100
        stop_time = 50
        price_move = 0.05
        price_stop = 0.02
        expected_total = (100 * 0.05) + (50 * 0.02)
        self.assertAlmostEqual(total_price(move_time, stop_time, price_move, price_stop), expected_total)

if __name__ == '__main__':
    unittest.main()
