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

    def in_order_traversal(self, node):
        if node is not None:
            if node.left is not None:
                self.in_order_traversal(node.left)
            print(node.player.player_name)
            if node.right is not None:
                self.in_order_traversal(node.right)



bst = PlayerBST()

# Insert 10 players
players = [
    Player("101", "Alex"),
    Player("102", "Ben"),
    Player("103", "Charlie"),
    Player("104", "David"),
    Player("105", "Emma"),
    Player("106", "Frank"),
    Player("107", "George"),
    Player("108", "Hannah"),
    Player("109", "Ian"),
    Player("110", "Jane")
]

for player in players:
    bst.insert(player)

# Print the players in sorted order (in-order traversal)
bst.in_order_traversal(bst.root)

# bst = PlayerBST()
# bst.insert(Player("101", "Alex"))
# bst.insert(Player("102", "Ben"))
# bst.insert(Player("103", "Charlie"))
# print(bst.root.right.root.right.root.player.player_name)
