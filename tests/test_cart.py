import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()

    def test_add_dvd_until_full(self):
        # Kiểm tra giới hạn 20 đĩa của giỏ hàng
        for i in range(20):
            self.assertTrue(self.cart.add_dvd(DigitalVideoDisc(f"DVD {i}")))
        self.assertFalse(self.cart.add_dvd(DigitalVideoDisc("DVD 21")))

    def test_sort_by_title(self):
        self.cart.add_dvd(DigitalVideoDisc("Zootopia", "Animation", "Director", 100, 20.0))
        self.cart.add_dvd(DigitalVideoDisc("Aladdin", "Animation", "Director", 90, 15.0))
        self.cart.sort_by_title()
        self.assertEqual(self.cart.items[0].title, "Aladdin")

    def test_sort_by_cost(self):
        self.cart.add_dvd(DigitalVideoDisc("Aladdin", "Animation", "Director", 90, 15.0))
        self.cart.add_dvd(DigitalVideoDisc("Zootopia", "Animation", "Director", 100, 20.0))
        self.cart.sort_by_cost()
        self.assertEqual(self.cart.items[0].title, "Zootopia")

    def test_discount(self):
        self.assertEqual(self.cart.total_cost_with_discount(100, 20), 80)

    def test_discount_invalid_percent(self):
        with self.assertRaises(ValueError):
            self.cart.total_cost_with_discount(100, 150)
