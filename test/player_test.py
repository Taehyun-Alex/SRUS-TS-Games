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


if __name__ == "__main__":
    unittest.main()