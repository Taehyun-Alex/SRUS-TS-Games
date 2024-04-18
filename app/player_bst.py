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
                node.left = PlayerBNode(player)  # Initialize left child as an empty PlayerBST object
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

    # def to_list(self):
    #     def inorder_traversal(node, lst):
    #         if node is not None:
    #             inorder_traversal(node.left, lst)
    #             lst.append(node.player)
    #             inorder_traversal(node.right, lst)
    #
    #     output = []
    #     inorder_traversal(self.root, output)
    #     return output  # returns a list of names

    def to_list(self, node, output=None):
        if output is None:
            output = []

        if node is not None:
            self.to_list(node.left, output)
            output.append(node.player)
            self.to_list(node.right, output)
        return output

    # def construct_balanced_bst(self, sorted_list):
    #     """
    #     takes bst object, finds the middle element,
    #     instantiate a new bst object,
    #     set the root node as middle element,
    #     traverse left and right to insert.
    #     """
    #     if sorted_list is None:
    #         return None
    #
    #     middle_index = len(sorted_list) // 2
    #     middle_item = sorted_list[middle_index]
    #     self._root = PlayerBNode(Player(middle_item.id, middle_item.player_name))
    #     self._root.left = self.construct_balanced_bst(sorted_list[:middle_index])
    #     self._root.right = self.construct_balanced_bst(sorted_list[middle_index + 1:])
    #
    #     return self._root

    @classmethod
    def construct_balanced_bst(cls, sorted_list):
        """
        takes bst object, finds the middle element,
        instantiate a new bst object,
        set the root node as middle element,
        traverse left and right to insert.
        """
        if sorted_list is None or len(sorted_list) == 0:
            return None

        middle_index = len(sorted_list) // 2
        middle_item = sorted_list[middle_index]

        root = PlayerBNode(middle_item)
        root.left = cls.construct_balanced_bst(sorted_list[:middle_index])
        root.right = cls.construct_balanced_bst(sorted_list[middle_index + 1:])

        return root


bst = PlayerBST()

bst.insert(Player("100", "Charlie"))
bst.insert(Player("101", "Alex"))
bst.insert(Player("102", "Ben"))
bst.insert(Player("103", "Mike"))
bst.insert(Player("104", "Kate"))
bst.insert(Player("105", "Peter"))
bst.insert(Player("106", "Aaron"))

print(bst.to_list(bst.root))  # returns a list of objects

sorted_list = bst.to_list(bst.root)
# balanced_bst = bst.construct_balanced_bst(sorted_list)
# print(balanced_bst.root.left.player.player_name)
obj = PlayerBST.construct_balanced_bst(sorted_list)
print(obj.left.player.player_name)
