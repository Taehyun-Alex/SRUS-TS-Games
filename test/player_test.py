import unittest
from app.player import Player


class TestTheProperties(unittest.TestCase):
    def setUp(self):
        self.player_temp = Player("103", "Jason")

    def test_player_instantiation(self):
        self.assertEqual(self.player_temp.uid, "103")
        self.assertEqual(self.player_temp.name, "Jason")

    def test_player_attribute_type(self):
        self.assertIsInstance(self.player_temp.uid, str)
        self.assertIsInstance(self.player_temp.name, str)


if __name__ == "__main__":
    unittest.main()