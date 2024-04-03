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
            if self._root.player.player_name > player.player_name:
                if self._root.left is None:
                    self._root.left = PlayerBST()  # Initialize left child as an empty PlayerBST object
                self._root.left.insert(player)  # Insert player into the left subtree
            elif self._root.player.player_name < player.player_name:
                if self._root.right is None:
                    self._root.right = PlayerBST()  # Initialize right child as an empty PlayerBST object
                self._root.right.insert(player)  # Insert player into the right subtree
            else:
                self._root = PlayerBNode(player)


bst = PlayerBST()
bst.insert(Player("101", "Alex"))
bst.insert(Player("102", "Ben"))
bst.insert(Player("103", "Charlie"))
bst.insert(Player("104", "Aaa"))

print(bst.root.right.root.right.root.player.player_name)
print(bst.root.left.root.player.player_name)
