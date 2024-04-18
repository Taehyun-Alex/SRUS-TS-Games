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

    def sorted_list_from_bst(self):
        def inorder_traversal(node, lst):
            if node is not None:
                inorder_traversal(node.left, lst)
                lst.append(node.player)
                inorder_traversal(node.right, lst)

        sorted_list = []
        inorder_traversal(self.root, sorted_list)
        return sorted_list  # returns a list of objects

    def print_sorted_list_of_objects(self):
        sorted_list = self.sorted_list_from_bst()
        output = ""
        for player in sorted_list:
            output += f"ID: {player.id}, Name: {player.player_name}\n"
        print(output)

    # https://chat.openai.com/share/1e082742-2747-49af-8c1e-ac034322cf54
    def construct_balanced_bst(self, sorted_list):
        if not sorted_list:
            return None

        middle_index = len(sorted_list) // 2
        middle_item = sorted_list[middle_index]
        self._root = PlayerBNode(middle_item)
        self._root.left = self.construct_balanced_bst(sorted_list[:middle_index])
        self._root.right = self.construct_balanced_bst(sorted_list[middle_index + 1:])

        return self._root


bst = PlayerBST()

bst.insert(Player("100", "Charlie"))
bst.insert(Player("101", "Alex"))
bst.insert(Player("102", "Ben"))
bst.insert(Player("103", "Mike"))
bst.insert(Player("104", "Kate"))
bst.insert(Player("105", "Peter"))
bst.insert(Player("106", "Aaron"))

print(bst.sorted_list_from_bst())
print(bst.construct_balanced_bst(bst.sorted_list_from_bst()))
