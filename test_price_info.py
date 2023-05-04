import unittest
from price_info import total_cost_shopping, cost_of_fruits

class TestPriceInfo(unittest.TestCase):

    def test_cost_of_fruits(self):
        # test for cost of single fruit
        self.assertEqual(cost_of_fruits('apple', 5), 6.0)
        self.assertEqual(cost_of_fruits('orange', 5), 7.0)
        self.assertEqual(cost_of_fruits('watermelon', 1), 6.5)
        self.assertEqual(cost_of_fruits('pineapple', 2), 5.4)
        self.assertEqual(cost_of_fruits('pear', 10), 9.0)
        self.assertEqual(cost_of_fruits('papaya', 1), 2.95)
        self.assertEqual(cost_of_fruits('pomegranate', 2), 9.9)
        # test for invalid fruit
        self.assertRaises(KeyError, cost_of_fruits, 'invalid_fruit', 5)

    def test_total_cost_shopping(self):
        # test for total cost of shopping
        self.assertEqual(total_cost_shopping(), 51.85)

if __name__ == '__main__':
    unittest.main()
