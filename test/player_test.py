import unittest
from app.player import Player


class TestTheProperties(unittest.TestCase):
    def setUp(self):
        self.player_temp = Player("103", "Jason")

    def test_player_instantiation(self):
        self.assertEqual(self.player_temp.id, "103")
        self.assertEqual(self.player_temp.player_name, "Jason")

    def test_player_attribute_type(self):
        self.assertIsInstance(self.player_temp.id, str)
        self.assertIsInstance(self.player_temp.player_name, str)


class TestPasswordVerification(unittest.TestCase):
    def setUp(self):
        self.player_temp = Player("104", "Mike")

    def test_password_verification(self):
        self.player_temp.add_password("a1b2c3d4")
        self.assertEqual(self.player_temp.verify_password("a1b2c3d4"), True)

    def test_password_verification_with_longer_password_input(self):
        self.player_temp.add_password("a29vkdm20sx2x03kfm84ifmv03wwwlw03")
        self.assertEqual(self.player_temp.verify_password("a29vkdm20sx2x03kfm84ifmv03wwwlw03"), True)


class TestScoreComparisonOperators(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("105", "Michael", 5)
        self.player_2 = Player("106", "Layla", 2)
        self.player_3 = Player("107", "Bec", 2)

    def test_equal_to(self):
        self.assertEqual(self.player_2 == self.player_3, True)

    def test_greater_than(self):
        self.assertEqual(self.player_1 > self.player_2, True)

    def test_less_than(self):
        self.assertEqual(self.player_3 < self.player_1, True)


class TestRadixSortReversedUsingScore(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("105", "Michael", 12)
        self.player_2 = Player("106", "Layla", 4)
        self.player_3 = Player("107", "Bec", 9)
        self.player_4 = Player("108", "Sydney", 4)

    def test_radix_sort_reversed_no_duplicates(self):
        self.assertEqual([12, 9, 4],
                         Player.radix_sort_in_descending_order(
                             [self.player_1.get_score(), self.player_2.get_score(), self.player_3.get_score()]
                         ))

    def test_radix_sort_reversed_with_duplicate_values(self):
        self.assertEqual([12, 4, 4],
                         Player.radix_sort_in_descending_order(
                             [self.player_1.get_score(), self.player_2.get_score(), self.player_4.get_score()]
                         ))


if __name__ == "__main__":
    unittest.main()
