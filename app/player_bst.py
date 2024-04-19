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
        if node is None:
            return PlayerBNode(player)  # Base case
        if node.player.player_name > player.player_name:
            node.left = self._insert_recursive(player, node.left)
        elif node.player.player_name < player.player_name:
            node.right = self._insert_recursive(player, node.right)
        else:
            node.player.player_name = player.player_name

        return node  # Return the passed argument, node, updated

    def search(self, name):
        if self._root is None or self._root == name:  # condition given from the assessment
            return name
        else:
            return self._search_recursive(self._root, name)

    def _search_recursive(self, node, name):
        if node is None:
            return False  # Base case
        if node.player.player_name == name:
            return True
        else:
            if node.player.player_name > name:
                return self._search_recursive(node.left, name)
            elif node.player.player_name < name:
                return self._search_recursive(node.right, name)

    def to_list(self, node, output=None):
        if output is None:
            output = []

        if node is not None:  # Inorder traverse method
            self.to_list(node.left, output)
            output.append(node.player)
            self.to_list(node.right, output)
        return output

    @classmethod
    def construct_balanced_bst(cls, sorted_list):
        if sorted_list is None or len(sorted_list) == 0:
            return None

        middle_index = len(sorted_list) // 2
        middle_item = sorted_list[middle_index]

        root = PlayerBNode(middle_item)
        root.left = cls.construct_balanced_bst(sorted_list[:middle_index])
        root.right = cls.construct_balanced_bst(sorted_list[middle_index + 1:])

        return root  # Returns the root of balanced BST, for access


bst = PlayerBST()
bst.insert(Player("100", "Charlie"))
bst.insert(Player("101", "Alex"))
bst.insert(Player("102", "Ben"))
bst.insert(Player("103", "Mike"))
bst.insert(Player("104", "Kate"))
bst.insert(Player("105", "Peter"))
bst.insert(Player("106", "Aaron"))


bst_list = bst.to_list(bst.root)

# classmethod function, no need to pass instantiated BST object, but wanted to test it
balanced_bst = PlayerBST.construct_balanced_bst(bst_list)
print(balanced_bst.player.player_name)  # Charlie. returns name attribute of root node of balanced bst
