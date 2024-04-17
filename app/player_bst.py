from player import Player
from player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self, root=None):
        self._root = root

    @property
    def root(self):
        return self._root

    def insert(self, player):
        if self._root is None:
            self._root = PlayerBNode(player)
        else:
            self._insert_recursive(player, self._root)

    def _insert_recursive(self, player, node):
        if node.player.player_name > player.player_name:
            if node.left is None:
                node.left = PlayerBNode(player)# Initialize left child as an empty PlayerBST object
            else:
                self._insert_recursive(player, node.left)  # Insert player into the left subtree
        elif node.player.player_name < player.player_name:
            if node.right is None:
                node.right = PlayerBNode(player)  # Initialize right child as an empty PlayerBST object
            else:
                self._insert_recursive(player, node.right)  # Insert player into the right subtree
        else:
            node.player.player_name = player.player_name
