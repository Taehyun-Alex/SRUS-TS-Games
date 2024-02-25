import unittest
from app.player_list import PlayerList
from app.player_node import PlayerNode
from app.player import Player


class TestInsertion(unittest.TestCase):
    def setUp(self):
        self.player_list = PlayerList()
        self.player_1 = Player("103", "Mark")
        self.player_node_1 = PlayerNode(self.player_1)
        self.player_2 = Player("104", "Kayla")
        self.player_node_2 = PlayerNode(self.player_2)

    def test_insert_node_at_head_when_empty_list(self):
        self.player_list.insert_at_head(self.player_node_1)
        self.assertEqual(self.player_1, self.player_list._head._player)

    def test_insert_node_at_head_when_non_empty_list(self):
        self.player_list.insert_at_head(self.player_node_1)
        self.player_list.insert_at_head(self.player_node_2)

        self.assertEqual(self.player_list._head._player, self.player_2)
        self.assertEqual(self.player_list._head._next._player, self.player_1)

    def test_tail_holds_value_of_first_item_added_when_insert_node_at_head(self):
        self.player_list.insert_at_head(self.player_node_1)
        self.player_list.insert_at_head(self.player_node_2)

        self.assertEqual(self.player_list._tail._player, self.player_1)

    def test_insert_at_tail_when_non_empty_list(self):
        self.player_list.insert_at_tail(self.player_node_1)
        self.player_list.insert_at_tail(self.player_node_2)

        self.assertEqual(self.player_list._tail._player, self.player_2)


if __name__ == "__main__":
    unittest.main()
