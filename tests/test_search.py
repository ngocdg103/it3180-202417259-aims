import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title, search_by_category

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.dvds = [
            DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95),
            DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 87, 24.95),
            DigitalVideoDisc("Aladdin", "Animation", cost=18.99),
        ]

    def test_search_by_title_case_insensitive(self):
        # Kiểm tra tìm kiếm không phân biệt hoa thường theo yêu cầu Lab 05
        results = search_by_title(self.dvds, "lion")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "The Lion King")

    def test_search_by_title_not_found(self):
        results = search_by_title(self.dvds, "Avatar")
        self.assertEqual(len(results), 0)

    def test_search_by_category(self):
        results = search_by_category(self.dvds, "Animation")
        self.assertEqual(len(results), 2)
