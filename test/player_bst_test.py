import unittest
from app.player_bst import PlayerBST
from app.player import Player

class TestBstInsertion(unittest.TestCase):

    def setUp(self):
        self.bst = PlayerBST()
        self.bst.insert(Player("100", "Charlie"))
        self.bst.insert(Player("101", "Alex"))
        self.bst.insert(Player("102", "Ben"))
        self.bst.insert(Player("103", "Mike"))
        self.bst.insert(Player("104", "Kate"))

    def test_bst_insertion_root(self):
        self.assertEqual(self.bst.root.player.player_name, "Charlie")

    def test_bst_insertion(self):
        self.assertEqual(self.bst.root.left.player.player_name, "Alex")
        self.assertEqual(self.bst.root.left.right.player.player_name, "Ben")
        self.assertEqual(self.bst.root.right.player.player_name, "Mike")
        self.assertEqual(self.bst.root.right.left.player.player_name, "Kate")


if __name__ == "__main__":
    unittest.main()