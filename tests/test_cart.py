import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

class TestCart(unittest.TestCase):
    def setUp(self):
        # Khởi tạo giỏ hàng trống trước khi chạy từng test case
        self.cart = Cart()

    def test_sort_by_title(self):
        self.cart.add_dvd(DigitalVideoDisc("Zootopia", "Animation", "Director", 100, 20.0))
        self.cart.add_dvd(DigitalVideoDisc("Aladdin", "Animation", "Director", 90, 15.0))
        self.cart.sort_by_title()
        # "Aladdin" chữ A đứng trước "Zootopia" chữ Z
        self.assertEqual(self.cart.items[0].title, "Aladdin")

    def test_sort_by_cost(self):
        self.cart.add_dvd(DigitalVideoDisc("Aladdin", "Animation", "Director", 90, 15.0))
        self.cart.add_dvd(DigitalVideoDisc("Zootopia", "Animation", "Director", 100, 20.0))
        self.cart.sort_by_cost()
        # Sắp xếp giá giảm dần nên 20.0 đứng trước 15.0
        self.assertEqual(self.cart.items[0].title, "Zootopia")
        
    # (Giữ nguyên các hàm test cũ của bạn ở dưới nếu có)