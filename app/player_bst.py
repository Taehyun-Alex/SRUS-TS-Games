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

    def search(self, name):
        if self._root is None or self._root == name:
            return name
        else:
            return self._search_recursive(self._root, name)

    def _search_recursive(self, node, name):
        if node is None:
            return False
        if node.player.player_name == name:
            return True
        else:
            if node.player.player_name > name:
                return self._search_recursive(node.left, name)
            elif node.player.player_name < name:
                return self._search_recursive(node.right, name)


bst = PlayerBST()

bst.insert(Player("100", "Charlie"))
bst.insert(Player("101", "Alex"))
bst.insert(Player("102", "Ben"))
bst.insert(Player("103", "Mike"))
bst.insert(Player("104", "Kate"))

print(bst.search("Kate"))